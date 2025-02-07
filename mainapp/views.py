from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PizzaForm, CheckoutForm
from .models import Cart, CartItem, OrderItem, Order
from datetime import datetime
from collections import defaultdict

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        orders = Order.objects.filter(user=request.user).order_by('-order_date')
        grouped_orders = defaultdict(list)

        for order in orders:
            order_date = order.order_date.date() # date without time
            grouped_orders[order_date].append(order)

        grouped_orders = sorted(grouped_orders.items(), key=lambda x: x[0], reverse=True)

        return render(request, "index.html", {"user": user, "grouped_orders": grouped_orders, "total_orders": len(orders)})
    return render(request, "index.html")


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the user
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


@login_required
def create_pizza(request):
    if request.method == "POST":
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            cart, created = Cart.objects.get_or_create(user=request.user)

            # check if pizza already exists in cart (duplicate) then just increase the quantity
            new_item = CartItem.objects.create(cart=cart, pizza=pizza)
            new_item.save()

            return redirect("view_cart")
    else:
        form = PizzaForm()
    return render(request, "create_pizza.html", {"form": form})


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, "cart.html", {"cart": cart})


@login_required
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id, cart__user=request.user)
    
    if request.method == "POST":
        cart_item.delete()
        messages.success(request, "The item has been removed from your cart.")
    else:
        messages.error(request, "Invalid request method.")
    
    return redirect("view_cart")


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # create the Order record with customer details from the form
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            # for each cart item, create an OrderItem
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    pizza=item.pizza,
                    quantity=item.quantity
                )

            # clear the cart after checkout
            cart.items.all().delete()
            return redirect("order_confirmation", id=order.id)
    else:
        form = CheckoutForm()
    
    if cart.items.all():
        return render(request, "checkout.html", {"form": form, "cart": cart})
    else:
        return redirect("/")


@login_required
def order_confirmation(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return redirect("/")
    
    if order.user != request.user:
        return redirect("/")

    order_items = order.order_items.all()
    print(order_items)
    return render(request, "order_confirmation.html", {"order": order, "order_items": order_items})
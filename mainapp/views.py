from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PizzaForm, CheckoutForm
from .models import Pizza, Cart, CartItem, OrderItem

# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required
def profile(request):
    return render(request, "profile.html")

    

def signup(request):
    if request.user.is_authenticated:
        return redirect("profile")

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Creates the user
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


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
            '''cart_item, item_created = CartItem.objects.get_or_create(cart=cart, pizza=pizza, defaults={"quantity": 1})
            if not item_created:
                cart_item.quantity += 1
            
            cart_item.save()'''

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
    
    if request.method == 'POST':
        cart_item.delete()
        messages.success(request, "The item has been removed from your cart.")
    else:
        messages.error(request, "Invalid request method.")
    
    return redirect('view_cart')


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create the Order record with customer details from the form.
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            # For each cart item, create an OrderItem.
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    pizza=item.pizza,
                    quantity=item.quantity
                )
            # Clear the cart after checkout
            cart.items.all().delete()
            return redirect('order_confirmation', order_id=order.pk)
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form, 'cart': cart})

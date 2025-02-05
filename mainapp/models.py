from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Size(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class CrustType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Sauce(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Cheese(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Pizza(models.Model):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(CrustType, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"{self.size} pizza with {self.crust} crust"
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.pizza}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", help_text="The user who placed the order")
    customer_name = models.CharField(max_length=100, help_text="The customer's name")
    address = models.CharField(max_length=200, help_text="The delivery address")
    card_number = models.CharField(max_length=16, help_text="Credit card number")
    card_expiry_month = models.CharField(max_length=2, help_text="Card expiry month")
    card_expiry_year = models.CharField(max_length=4, help_text="Card expiry year")
    card_cvv = models.CharField(max_length=3, help_text="Card CVV code")
    order_date = models.DateTimeField(auto_now_add=True, help_text="Date and time when the order was placed")

    def __str__(self):
        return f"Order {self.pk} by {self.customer_name}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.pizza} in Order {self.order.pk}"
from django import forms
from .models import Pizza, Order

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ["size", "crust", "sauce", "cheese", "toppings"]
        widgets = {
            "toppings": forms.CheckboxSelectMultiple(),
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "address", "card_number", "card_expiry_month", "card_expiry_year", "card_cvv"]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Delivery address"}),
            "card_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Credit Card Number"}),
            "card_expiry_month": forms.TextInput(attrs={"class": "form-control", "placeholder": "MM"}),
            "card_expiry_year": forms.TextInput(attrs={"class": "form-control", "placeholder": "YYYY"}),
            "card_cvv": forms.TextInput(attrs={"class": "form-control", "placeholder": "CVV"}),
        }
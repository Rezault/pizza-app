from django import forms
from .models import Pizza, Order, Topping
from datetime import datetime

class PizzaForm(forms.ModelForm):
    toppings = forms.ModelMultipleChoiceField(
        queryset=Topping.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=False
    )

    class Meta:
        model = Pizza
        fields = ["size", "crust", "sauce", "cheese", "toppings"]


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "address", "card_number", "card_expiry_month", "card_expiry_year", "card_cvv"]
        widgets = {
            "customer_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Your full name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Delivery address"}),
            # bit of research done into forms and widgets
            # type tel is for mobile users, force numeric keypad
            "card_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Credit Card Number",
                "type": "tel",
                "inputmode": "numeric",
                "pattern": "[0-9]{16}",
                "title": "Enter a valid 16-digit credit card number."
            }),
            "card_expiry_month": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "MM",
                "type": "tel",
                "inputmode": "numeric",
                "pattern": "0[1-9]|1[0-2]",
                "title": "Enter a valid month (01 - 12)."
            }),
            "card_expiry_year": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "YYYY",
                "type": "tel", 
                "inputmode": "numeric",
                "pattern": "[0-9]{4}",
                "title": "Enter a valid 4-digit year."
            }),
            "card_cvv": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "CVV",
                "type": "tel",
                "inputmode": "numeric",
                "pattern": "[0-9]{3}",
                "title": "Enter a valid 3-digit CVV code."
            }),
        }

    # functions for data validation
    # widgets and javascript validation seems like it's enough, but it prevent bypass
    # luckily, django offers a backend validation with these "clean_" methods
    # found out about these with a bit of research, they're very useful
    def clean_card_number(self):
        card_number = self.cleaned_data.get("card_number")
        if not card_number.isdigit():
            raise forms.ValidationError("Card number must contain only digits.")
        if len(card_number) != 16:
            raise forms.ValidationError("Card number must be 16 digits.")
        return card_number

    def clean_card_expiry_month(self):
        month = self.cleaned_data.get("card_expiry_month")
        if not month.isdigit() or not (1 <= int(month) <= 12):
            raise forms.ValidationError("Enter a valid month (01 - 12).")
        return month

    def clean_card_expiry_year(self):
        year = self.cleaned_data.get("card_expiry_year")
        if not year.isdigit() or len(year) != 4:
            raise forms.ValidationError("Enter a valid 4-digit year.")
        return year

    def clean_card_cvv(self):
        cvv = self.cleaned_data.get("card_cvv")
        if not cvv.isdigit() or len(cvv) != 3:
            raise forms.ValidationError("CVV must be 3 digits long.")
        return cvv
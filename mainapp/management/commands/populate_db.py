from django.core.management.base import BaseCommand
from mainapp.models import Size, CrustType, Topping, Cheese, Sauce

class Command(BaseCommand):
    help = "Populate the database with default pizza options."

    def handle(self, *args, **kwargs):
        Size.objects.get_or_create(name="Small")
        Size.objects.get_or_create(name="Medium")
        Size.objects.get_or_create(name="Large")
        Size.objects.get_or_create(name="Extra Large")

        CrustType.objects.get_or_create(name="Normal")
        CrustType.objects.get_or_create(name="Thin")
        CrustType.objects.get_or_create(name="Thick")
        CrustType.objects.get_or_create(name="Gluten Free")

        Cheese.objects.get_or_create(name="Mozzarella")
        Cheese.objects.get_or_create(name="Cheddar")
        Cheese.objects.get_or_create(name="Gouda")
        Cheese.objects.get_or_create(name="Low Fat")
        Cheese.objects.get_or_create(name="Vegan")

        Sauce.objects.get_or_create(name="Tomato")
        Sauce.objects.get_or_create(name="BBQ")

        Topping.objects.get_or_create(name="Pepperoni")
        Topping.objects.get_or_create(name="Chicken")
        Topping.objects.get_or_create(name="Ham")
        Topping.objects.get_or_create(name="Pineapple")
        Topping.objects.get_or_create(name="Peppers")
        Topping.objects.get_or_create(name="Mushrooms")
        Topping.objects.get_or_create(name="Onions")
        Topping.objects.get_or_create(name="Sweetcorn")
        Topping.objects.get_or_create(name="Tuna")
        Topping.objects.get_or_create(name="Bacon")
        
        self.stdout.write(self.style.SUCCESS("✅ Default pizza options added!"))

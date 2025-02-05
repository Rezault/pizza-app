from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Size)
admin.site.register(models.CrustType)
admin.site.register(models.Sauce)
admin.site.register(models.Cheese)
admin.site.register(models.Topping)
admin.site.register(models.Pizza)
admin.site.register(models.Order)
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Size)
admin.site.register(models.CrustType)
admin.site.register(models.Sauce)
admin.site.register(models.Cheese)
admin.site.register(models.Topping)
admin.site.register(models.Pizza)

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0
    readonly_fields = ("pizza", "quantity")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "user", "order_date")
    inlines = [OrderItemInline]

admin.site.register(models.Order, OrderAdmin)

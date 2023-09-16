from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class ModelNameAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class ModelNameAdmin(admin.ModelAdmin):
    pass
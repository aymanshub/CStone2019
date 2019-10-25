from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'total_cost',
                    'discount_percentage', 'created']

    list_editable = ['status', 'discount_percentage']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'item_cost', 'quantity',
                    'discount_percentage']
    list_editable = ['discount_percentage']

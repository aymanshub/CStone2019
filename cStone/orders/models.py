from decimal import Decimal

from django.db import models
from main.models import Product
from customers.models import Customer


class Order(models.Model):
    STATUS_CHOICES = [
        ('paid', 'שולם'),
        ('open', 'פתוח'),
        ('rfs', 'מוכן למשלוח'),
        ('canceled', 'מבוטל'),
        ('quote', 'הצעת מחיר')
    ]

    customer = models.ForeignKey(Customer, related_name='orders',
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default='open',
    )

    discount_percentage = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    @property
    def total_cost(self):

        calculation = (
                sum(
                    item.item_cost for item in self.items.all()
                ) *
                (1-(Decimal(self.discount_percentage/100)))
        )

        return round(calculation, 2)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    discount_percentage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Order {} Item {}'.format(self.order.id, self.id)

    @property
    def item_cost(self):
        calculation = (
                self.product.price *
                (1-(Decimal(self.discount_percentage/100))) *
                self.quantity
        )

        return round(calculation, 2)

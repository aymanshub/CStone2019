from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from orders.models import Order, OrderItem

# Create your views here.


def new_quote(request):
    new_order = Order.objects.create(status='quote')

    # return render(request, r,
    #               {'form': form, 'course': course})
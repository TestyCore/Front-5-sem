import os

import matplotlib
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from matplotlib import pyplot as plt

from Lab_4 import settings
from order.models import Order


def client_list(request):
    usrs = User.objects.all()

    usrs = usrs.exclude(username="Asik")
    usrs = usrs.exclude(username="Batya")


    return render(request, 'client_list/client_list.html', {'usrs': usrs})


def client_detail(request, client_id):
    usrs = User.objects.all()
    usr = usrs.filter(id=client_id).first()

    orders = Order.objects.filter(client=usr.id).prefetch_related('items')

    orders_list = [
        {
            'order': order.created,
            'order_items': [[item.product.title.__str__() + ' $' + item.price.__str__() + ', ' + item.quantity.__str__() + 'pc.'] for item in order.items.all()]
        }
        for order in orders
    ]

    return render(request, 'client_list/client_detail.html', {'usr': usr, 'ordrs': orders_list})









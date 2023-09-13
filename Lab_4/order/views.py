# from /Users/brr/Library/Python/3.9/lib/python/site-packages/requests

from django.db.models import Sum, Avg, Count
from django.shortcuts import render, redirect
from django.views import generic
from statistics import mode, median
import requests
import json
import base64
import uuid

from .models import OrderItem, Order
from cart.cart import Cart
from django.core.exceptions import PermissionDenied


import logging
logger = logging.getLogger(__name__)


def order_create(request):
    if not request.user.is_authenticated:
        raise PermissionDenied("net dostpa")

    cart = Cart(request)
    if cart.get_total_price() == 0:
        return redirect('http://127.0.0.1:8000/edostavka/products/')
    if request.method == 'POST':
        order = Order.objects.create(client=request.user)

        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
            item['product'].save()

        url = "https://api.yookassa.ru/v3/payments"

        shop_id = "318870"
        secret_key = "test_e6oCux8C5T90AegU9ba_zWHoW0BDVkiQowMv9xV4Ha0"

        headers = {
            "Authorization": "Basic " + base64.b64encode(f"{shop_id}:{secret_key}".encode("utf-8")).decode("utf-8"),
            "Idempotence-Key": str(uuid.uuid4()),
            "Content-Type": "application/json"
        }

        payload = {
            "amount": {
                "value": cart.get_total_price().__str__(),
                "currency": "RUB"
            },
            "capture": "true",
            "confirmation": {
                "type": "redirect",
                "return_url": "http://127.0.0.1:8000/edostavka/products/",
                "confirm_url": "https://localhost:7185/Cart/Index"
            }
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response_data = response.json()

        logger.info('Purchase completed!')

        cart.clear()

        if response.ok:
            redirect_url = response_data["confirmation"]["confirmation_url"]
            return redirect(redirect_url)
        else:
            logger.error('Purchase Failed')
            raise Exception("Failed to initiate payment. Error: " + response.text)

    return render(request, 'order/create.html', {'cart': cart})


class OrderListView(generic.ListView):
    model = Order
    queryset = Order.objects.order_by('client')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        total_cost = 0
        for order in orders:
            total_cost = total_cost + order.get_total_cost()

        print(total_cost)
        order_count = Order.objects.count()
        print(order_count)
        average_cost = total_cost / order_count if order_count > 0 else 0
        order_prices = Order.objects.values_list('items__price', flat=True)
        mode_cost = mode(order_prices) if order_prices else 0

        most_common_item = Order.objects.values('items__product__title').annotate(
            count=Count('items__product__title')).order_by('-count').first()
        most_common_item_name = most_common_item['items__product__title'] if most_common_item else ''

        context['total_cost'] = "{:.2f}".format(total_cost or 0)
        context['average_cost'] = "{:.2f}".format(average_cost or 0)
        context['mode_cost'] = "{:.2f}".format(mode_cost or 0)
        context['most_common_item_name'] = most_common_item_name

        return context

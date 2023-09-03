

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from order.models import Order
from order.models import OrderItem


def client_list(request):
    usrs = User.objects.all()

    usrs = usrs.exclude(username="Asik")
    usrs = usrs.exclude(username="Batya")

    return render(request, 'client_list/client_list.html', {'usrs': usrs})


def client_detail(request, client_id):
    usrs = User.objects.all()
    usr = usrs.filter(id=client_id).first()
    # ordrs = Order.objects.all()
    # ordrs = [[item.id, item.client, item.created] for item in ordrs]
    #
    # order_items = OrderItem.objects.all()
    #
    # for ordr in ordrs:
    #     items = order_items.filter(order_id=ordr[0])
    #     items = list(items)
    #     items = items[1:4]
    #     ordr.append(items)
    #     ordr = ordr[2:]
    #     a = 5

    orders = Order.objects.filter(client=usr.username).prefetch_related('items')

    orders_list = [
        {
            'order': order.created,
            'order_items': [[item.product.title.__str__() + ' $' + item.price.__str__() + ', ' + item.quantity.__str__() + 'pc.'] for item in order.items.all()]
        }
        for order in orders
    ]
    a = 5

    return render(request, 'client_list/client_detail.html', {'usr': usr, 'ordrs': orders_list})


















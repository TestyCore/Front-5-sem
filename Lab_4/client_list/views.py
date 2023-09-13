from django.db.models import Count
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

    orders = Order.objects.filter(client=usr.id).prefetch_related('items')

    orders_list = [
        {
            'order': order.created,
            'order_items': [[item.product.title.__str__() + ' $' + item.price.__str__() + ', ' + item.quantity.__str__() + 'pc.'] for item in order.items.all()]
        }
        for order in orders
    ]

    data = (
        Order.objects.annotate(day_count=Count('created'))
        .values('created', 'day_count')
        .order_by('created')
    )

    # dates = [entry['created'] for entry in data]
    # sales_count = [entry['day_count'] for entry in data]

    dates = ['2023-09-01', '2023-09-02', '2023-09-03']

    sales_count = [10, 15, 20]

    return render(request, 'client_list/client_detail.html', {'usr': usr, 'ordrs': orders_list, 'dates': dates, 'sales_count': sales_count})


















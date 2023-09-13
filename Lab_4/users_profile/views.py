from django.shortcuts import render, redirect

from order.models import Order
from back_info.models import Review
from django.utils import timezone
from datetime import datetime, timedelta
import pytz


import logging
logger = logging.getLogger(__name__)


def users_profile(request):
    user = request.user

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        user.save()
        logger.info('User profile info was changed')
        return redirect('users_profile:users_profile')

    orders = Order.objects.filter(client=user.id).prefetch_related('items')

    orders_list = [
        {
            'date': order.created,
            'order_items': [[item.product.title.__str__() + ' $' + item.price.__str__() + ', ' + item.quantity.__str__() + 'pc.'] for item in order.items.all()]
        }
        for order in orders
    ]
    is_customer = request.user.groups.filter(name='Customer').exists()
    reviews = Review.objects.filter(client_id=user.id)

    desired_timezone = pytz.timezone('Europe/Minsk')
    timezone.activate(desired_timezone)
    current_datetime = timezone.now().strftime('%d/%m/%Y')
    current_timezone = timezone.get_current_timezone()

    context = {
        'user': user,
        'orders': orders_list,
        'reviews': reviews,
        'is_customer': is_customer,
        'current_datetime': current_datetime,
        'current_timezone': current_timezone
    }

    return render(request, 'users_profile/profile.html', context=context)

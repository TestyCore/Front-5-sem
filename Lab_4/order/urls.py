from . import views
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
]

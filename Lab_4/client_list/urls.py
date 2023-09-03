
from django.urls import path
from . import views

app_name = 'client_list'

urlpatterns = [
    path('client_list/', views.client_list, name='client_list'),
    path('client_detail/<int:client_id>/', views.client_detail, name='client_detail'),
]


from django.urls import path
from . import views

app_name = 'users_profile'

urlpatterns = [
    path('users_profile/', views.users_profile, name='users_profile'),
]

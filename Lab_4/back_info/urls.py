from django.urls import path
from . import views

app_name = 'back_info'

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('news/', views.news, name='news'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('contacts/', views.contacts, name='contacts'),
    path('policy/', views.policy, name='policy'),
    path('reviews/', views.reviews, name='reviews'),
]

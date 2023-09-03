from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path(r'^product/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product-detail'),
    path('register/', register, name='register'),
]

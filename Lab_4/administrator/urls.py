from django.urls import path

import administrator.views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'administrator'

urlpatterns = [
    path('/', views.index, name='list_product'),
    path('create/', administrator.views.ProductCreate.as_view(), name='create_product'),
    path('delete/<int:id>/', administrator.views.ProductDelete.as_view(), name='delete_product'),
    path('edit/<int:id>/', administrator.views.ProductEdit.as_view(), name='edit_product'),
]

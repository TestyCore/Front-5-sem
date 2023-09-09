from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.views.generic import RedirectView

from Lab_4 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('back_info/', include('back_info.urls', namespace='back_info')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('client_list/', include('client_list.urls', namespace='client_list')),
    path('users_profile/', include('users_profile.urls', namespace='users_profile')),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('edostavka/', include('edostavka.urls')),
    path('', RedirectView.as_view(url='edostavka/')),
    path('accounts/', include('django.contrib.auth.urls')),
]

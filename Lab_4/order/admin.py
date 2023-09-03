from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client',
                    'created']
    list_filter = ['created']
    inlines = [OrderItemInline]  # Это список встроенных представлений, которые будут отображаться на странице
    # заказа. В данном случае, используется OrderItemInline, чтобы отображать элементы заказа внутри страницы заказа.


admin.site.register(Order, OrderAdmin)

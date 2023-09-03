from django.core.exceptions import PermissionDenied

import requests

from .forms import ExtendedUserCreationForm
from .models import Product, Manufacturer
from django.views import generic

from django.contrib.auth import login
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import Group

# Define the user roles
UNAUTHORIZED_ROLE = 'Unauthorized'
CUSTOMER_ROLE = 'Customer'
STAFF_ROLE = 'Staff'
ADMIN_ROLE = 'Admin'


def group_required(group_names):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=group_names).exists():
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied("Access denied.")
        return wrapper
    return decorator


# def group_required_class(group_names):
#     def decorator(view_class):
#         decorated_view = user_passes_test(lambda user: user.groups.filter(name__in=group_names).exists())(view_class)
#         return method_decorator(login_required(login_url='login'))(decorated_view)
#     return decorator


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign the appropriate role based on the form data
            user_role = form.cleaned_data['user_role']
            if user_role == 'staff':
                group = Group.objects.get_or_create(name='Staff')[0]
                user.groups.add(group)
            elif user_role == 'administrator':
                group = Group.objects.get_or_create(name='Admin')[0]
                user.groups.add(group)
            else:
                group = Group.objects.get_or_create(name='Customer')[0]
                user.groups.add(group)
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# @group_required(['Customer'])
def index(request):
    products = Product.objects.all()
    num_products = products.count()
    num_manufacturers = Manufacturer.objects.all().count()

    # context = {
    #     'num_products': num_products,
    #     'num_manufacturers': num_manufacturers,
    # }

    try:
        response = requests.get('https://api.kanye.rest/')
        if response.status_code == 200:
            data = response.json()
            quote = data["quote"]
        else:
            quote = "Failed to retrieve quote."

    except:
        quote = ""

    context = {
        'num_products': num_products,
        'num_manufacturers': num_manufacturers,
        'quote': quote,
    }

    return render(request, 'index.html', context=context)


# @group_required_class(['Customer'])
class ProductsListView(generic.ListView):
    model = Product
    # paginate_by = 5

    # template_name = 'product_list.html'  # Specify the template name

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_type = self.request.GET.get('filter_type')
        sort_order = self.request.GET.get('sort_order')

        if filter_type == 'name':
            if sort_order == 'ascending':
                queryset = queryset.order_by('title')
            elif sort_order == 'descending':
                queryset = queryset.order_by('-title')
        elif filter_type == 'price':
            if sort_order == 'ascending':
                queryset = queryset.order_by('price')
            elif sort_order == 'descending':
                queryset = queryset.order_by('-price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_name'] = self.request.GET.get('filter_name')
        context['filter_price'] = self.request.GET.get('filter_price')
        return context


# @group_required_class(['Customer'])
class ProductDetailView(generic.DetailView):
    model = Product







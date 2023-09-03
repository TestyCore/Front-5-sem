from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import ProductForm
from .templates import administrator
from edostavka.models import Product


@user_passes_test(lambda user: user.groups.filter(name='Admin').exists())
def index(request):
    products = Product.objects.all()
    return render(request, "administrator/list_product.html", {"products": products})


class ProductCreate(UserPassesTestMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'administrator/create_product.html', {'form': form})

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrator:list_product')
        return render(request, 'administrator/create_product.html', {'form': form})


class ProductEdit(UserPassesTestMixin, View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(instance=product)
        return render(request, 'administrator/edit_product.html', {'product': product, 'form': form})

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('administrator:list_product')
        return render(request, 'administrator/edit_product.html', {'product': product, 'form': form})


class ProductDelete(UserPassesTestMixin, View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect('administrator:list_product')

    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()

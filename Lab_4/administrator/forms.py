from django import forms
from edostavka.models import Product, ProductCategory, Manufacturer


class ProductForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(
        queryset=ProductCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    manufacturer = forms.ModelChoiceField(
        queryset=Manufacturer.objects.all().exclude(name='------')
    )

    class Meta:
        model = Product
        fields = ('title', 'category', 'price', 'composition', 'ean', 'manufacturer')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['category'].initial = self.instance.category.all()

    def clean_price(self):
        price = self.cleaned_data.get('price')
        price = str(price)
        if not float(price):
            raise forms.ValidationError('Price must contain only numbers.')
        return price

    def clean_ean(self):
        ean = self.cleaned_data.get('ean')
        ean = str(ean)
        if not ean.isdigit():
            raise forms.ValidationError('EAN must contain only numbers.')
        if not len(ean) == 13:
            raise forms.ValidationError('EAN must contain 13 numbers.')
        return ean

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('At least one category must be chosen.')
        return category

    def save(self, commit=True):
        product = super().save(commit=False)  # Эта строка вызывает метод save родительского класса (класса-предка
        # формы) с параметром commit=False. commit=False означает, что объект product будет создан, но не будет
        # сохранен в базе данных.
        if commit:
            product.save()
        if self.cleaned_data['category']:
            a = self.cleaned_data['category']
            product.category.set(self.cleaned_data['category'])
        else:
            product.category.clear()
        self.save_m2m()
        return product

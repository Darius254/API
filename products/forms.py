from django import forms
from .models import Product, Variant

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

class VariantForm(forms.ModelForm):
    class Meta:
        model = Variant
        fields = ['product', 'name']

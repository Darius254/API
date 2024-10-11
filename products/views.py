from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .models import Product,Variant
from .serializers import ProductSerializer
from .forms import ProductForm, VariantForm

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def product_list(request):
    products = Product.objects.prefetch_related('variants').all()
    return render(request, 'products/index.html', {'products': products})

def product_list(request):
    products = Product.objects.prefetch_related('variants').all()
    product_form = ProductForm()
    variant_form = VariantForm()

    if request.method == 'POST':
        if 'create_product' in request.POST:
            product_form = ProductForm(request.POST)
            if product_form.is_valid():
                product_form.save()
                return redirect('product_list')
        elif 'create_variant' in request.POST:
            variant_form = VariantForm(request.POST)
            if variant_form.is_valid():
                variant_form.save()
                return redirect('product_list')

    return render(request, 'products/index.html', {
        'products': products,
        'product_form': product_form,
        'variant_form': variant_form
    })

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')

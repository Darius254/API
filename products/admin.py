from django.contrib import admin
from .models import Product, Variant

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1  # Number of empty forms for variants

class ProductAdmin(admin.ModelAdmin):
    inlines = [VariantInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Variant)

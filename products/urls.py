from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,product_list,delete_product

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', product_list, name='product_list'),
    path('products/delete/<int:pk>/', delete_product, name='delete_product'),
]

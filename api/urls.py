from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet


# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)
#
# urlpatterns = [
#    path('', include(router.urls)),
# ]

############################
from .views import CategoryList, CategoryDetail, ProductList, ProductDetail
urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
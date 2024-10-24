from django.urls import path
from .views import (ProductListView, ProductCreateView, ProductDetailView,
                    ProductUpdateView, ProductDeleteView,
                    CategoryCreateView, CategoryListView, CategoryDetailView,
                    CategoryUpdateView, CategoryDeleteView)
from .views import ProductListByCategory, product_search
from cart.views import cart_add

urlpatterns = [
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/<slug:slug>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('categories/<slug:slug>/products/', ProductListByCategory.as_view(), name='products_by_category'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),


    path('search/', product_search, name="product_search"),
    path('list/', ProductListView.as_view(), name='products'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('<slug:slug>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('<slug:slug>/addToCart/', cart_add, name='add_to_cart'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),

    path('', ProductListByCategory.as_view(), name='index'),





]
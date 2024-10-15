from django.urls import path
from .views import (ProductListView, ProductCreateView,
                    CategoryCreateView, CategoryListView, CategoryDetailView)


urlpatterns = [
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
    path('products/', ProductListView.as_view(), name='products'),

    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/', CategoryListView.as_view(), name='categories'),

]
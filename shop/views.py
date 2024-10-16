from django.views.generic import (ListView, CreateView,
                                  UpdateView, DetailView,
                                  DeleteView, TemplateView)

from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Product, Category
from .forms import CategoryCreateForm, ProductCreateForm


class AdminTemplateView(TemplateView):
    template_name = 'shop/admin.html'


class IndexTemplateView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        products = Product.objects.all()
        context['categories'] = categories
        context['products'] = products

        return context


class ProductListByCategory(ListView):
    model = Product
    template_name = 'shop/products_by_category.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories

        return context

    def get_queryset(self):
        # Получаем категорию по slug из URL
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=category)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'shop/admin/product_add.html'
    success_url = reverse_lazy('products')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/admin/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'


class ProductListView(ListView):
    model = Product
    template_name = 'shop/admin/products.html'
    context_object_name = 'products'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'shop/admin/product_edit.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shop/admin/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('products')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'shop/admin/category_add.html'
    success_url = reverse_lazy('categories')


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/admin/categories.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/admin/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'shop/admin/category_edit.html'
    context_object_name = 'category'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'shop/admin/category_delete.html'
    context_object_name = 'category'
    success_url = reverse_lazy('categories')
import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.form.initial['price_min'] = 50

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    order_by = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('price', 'price'),
        )
    )

    class Meta:
        model = Product

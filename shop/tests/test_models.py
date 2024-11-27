from django.test import TestCase
from shop.models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="phones", slug="phones")

    def test_categories_name(self):
        phones = Category.objects.get(name="phones")
        self.assertEqual(phones.name, 'phones')

    def test_categories_slug(self):
        phones = Category.objects.get(name="phones")
        self.assertEqual(phones.slug, 'phones')

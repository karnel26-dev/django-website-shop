from django.test import TestCase
from django.urls import reverse


class CategoryListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/products/categories/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('categories'))
        self.assertEqual(resp.status_code, 200)

    def test_categories_set_in_context(self):
        resp = self.client.get(reverse('categories'))
        self.assertTrue('categories' in resp.context)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('categories'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'shop/admin/categories.html')

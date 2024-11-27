from django.test import TestCase
from shop.forms import CategoryCreateForm


class CategoryCreateFormTest(TestCase):
    def test_field_label(self):
        form = CategoryCreateForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Категория')

    def test_form_valid(self):
        form_data = {'name': 'phones'}
        form = CategoryCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
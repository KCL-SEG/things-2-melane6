from django import forms
from django.test import TestCase
from things.forms import ThingForm
from things.models import Thing

class ThingFormTestCase(TestCase):
    """Unit testing class the sign up forms"""
    def setUp(self):
        self.form_input = {
            'name': 'Example_thing',
            'description': 'Example things description',
            'quantity': 4
        }
    def test_valid_sign_up(self):
        form = ThingForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessart_fields(self):
        form = ThingForm()
        self.assertIn('name', form.fields)
        self.assertIn('description', form.fields)
        self.assertIn('quantity', form.fields)

        quantity_field = form.fields['quantity']
        self.assertTrue(isinstance(quantity_field, forms.IntegerField))

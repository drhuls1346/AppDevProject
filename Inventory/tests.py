"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from.views import HomeView


class urlTests(TestCase):
    def test_home_url(self):
        home = resolve(reverse('inv_templates:home'))
        return self.assertEqual(home.func.__name__,
                                HomeView.__name__)

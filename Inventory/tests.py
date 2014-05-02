"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from.views import HomeView, Add_ItemView, Remove_ItemView, Update_ItemView, Check_Out_ItemView, Check_In_ItemView


class urlTests(TestCase):
    def test_home_url(self):
        home = resolve(reverse('inv_templates:home'))
        return self.assertEqual(home.func.__name__,
                                HomeView.__name__)

class urlTests(TestCase):
    def test_add_item_url(self):
        add_item = resolve(reverse('inv_templates:add_item'))
        return self.assertEqual(add_item.func.__name__,
                                Add_ItemView.__name__)

class urlTests(TestCase):
    def test_remove_item_url(self):
        remove_item = resolve(reverse('inv_templates:remove_item'))
        return self.assertEqual(remove_item.func.__name__,
                                Remove_ItemView.__name__)

class urlTests(TestCase):
    def test_update_item_url(self):
        update_item = resolve(reverse('inv_templates:update_item'))
        return self.assertEqual(update_item.func.__name__,
                                Update_ItemView.__name__)

class urlTests(TestCase):
    def test_check_out_item_url(self):
        check_out_item = resolve(reverse('inv_templates:check_out_item'))
        return self.assertEqual(check_out_item.func.__name__,
                                Check_Out_ItemView.__name__)

class urlTests(TestCase):
    def test_check_in_item_url(self):
        check_in_item = resolve(reverse('inv_templates:check_in_item'))
        return self.assertEqual(check_in_item.func.__name__,
                                Check_in_ItemView.__name__)
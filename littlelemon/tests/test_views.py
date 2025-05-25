from django.test import TestCase
from django.urls.base import reverse

from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        # This method will be called before each test_ method below.
        # Create some MenuItem instances that can be used by multiple tests.
        self.menu_item1 = MenuItem.objects.create(title="Ice Cream", price=5.00, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Cake", price=8.50, inventory=50)
        self.menu_item3 = MenuItem.objects.create(title="Soda", price=2.00, inventory=200)


    def test_getall(self):

        all_items = MenuItem.objects.all()
        self.assertEqual(all_items.count(), 3)
        self.assertIn(self.menu_item1, all_items)
        self.assertIn(self.menu_item2, all_items)
        self.assertIn(self.menu_item3, all_items)

        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
        item_json = [{'id': 1, 'title': 'Ice Cream', 'price': '5.00', 'inventory': 100}, {'id': 2, 'title': 'Cake', 'price': '8.50', 'inventory': 50}, {'id': 3, 'title': 'Soda', 'price': '2.00', 'inventory': 200}]
        self.assertEqual(response.json(), item_json)

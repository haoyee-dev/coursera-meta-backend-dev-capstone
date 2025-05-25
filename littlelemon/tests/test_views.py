from django.test import TestCase

from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        # This method will be called before each test_ method below.
        # Create some MenuItem instances that can be used by multiple tests.
        self.menu_item1 = MenuItem.objects.create(title="Ice Cream", price=5.00, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Cake", price=8.50, inventory=50)
        self.menu_item3 = MenuItem.objects.create(title="Soda", price=2.00, inventory=200)

    # You can also set up other things, like a test client if you're testing views
    # from django.test import Client
    # self.client = Client()

    def test_getall(self):
        # Now you can use the objects created in setUp()
        # For example, if you have a view that lists all menu items:
        # response = self.client.get(reverse('menu-list')) # Assuming you have a URL named 'menu-list'
        # self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Let's assume we are directly testing the model count for simplicity here
        # or checking if the items created in setUp are present
        all_items = MenuItem.objects.all()
        self.assertEqual(all_items.count(), 3)
        self.assertIn(self.menu_item1, all_items)
        self.assertIn(self.menu_item2, all_items)
        self.assertIn(self.menu_item3, all_items)
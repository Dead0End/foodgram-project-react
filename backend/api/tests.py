from http import HTTPStatus

from django.test import Client, TestCase


class FoodgramAPITestCase(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_recipe_list_exists(self):
        response = self.guest_client.get('/api/recipes/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
from django.test import TestCase
from django.urls import reverse

class PoloViewTest(TestCase):
    def test_polo_view_response(self):
        response = self.client.get(reverse('polo'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Polo")

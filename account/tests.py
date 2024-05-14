from django.urls import reverse
from rest_framework.test import APITestCase
from .models import UserData


class UserDataAPITests(APITestCase):
    def test_create_user(self):
        url = reverse('sign_up')
        data = {
            'name': 'opopop',
            'email': 'opopop@gmail.com',
            'password': 'admin'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 201)  # Check for HTTP 201 Created
        self.assertEqual(UserData.objects.count(), 1)
        self.assertEqual(UserData.objects.get().name, 'opopop')
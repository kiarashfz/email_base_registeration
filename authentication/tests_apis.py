from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
import base64
from authentication.models import User


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('authentication.urls')),
    ]

    admin_email = 'admin@admin.admin'
    admin_password = 'admin'

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser(cls.admin_email, cls.admin_password)
        super().setUpTestData()

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user-list')
        data = {
            'email': 'test@test.test',
            'password': 'test'
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['id'], 2)  # Expected id is 2 because id 1 is superuser

    def test_get_all_users(self):
        """
        Ensure superuser can get all user objects.
        """
        url = reverse('user-list')

        # Using Basic authentication
        username_password = f'{self.admin_email}:{self.admin_password}'.encode()
        encoded_data = str(base64.b64encode(username_password).decode())
        self.client.credentials(HTTP_AUTHORIZATION=f"Basic {encoded_data}")

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

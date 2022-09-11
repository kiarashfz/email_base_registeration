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

    user_email = 'user@user.user'
    user_password = 'user'

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(cls.admin_email, cls.admin_password)
        cls.user = User.objects.create_user(cls.user_email, cls.user_password)
        super().setUpTestData()

    def set_basic_authentication(self, is_admin: bool) -> User:
        username_password = f'{self.admin_email}:{self.admin_password}'.encode() if is_admin else f'{self.user_email}:{self.user_password}'.encode()
        encoded_data = str(base64.b64encode(username_password).decode())
        self.client.credentials(HTTP_AUTHORIZATION=f"Basic {encoded_data}")
        return self.admin if is_admin else self.user

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

    def test_get_all_users(self):
        """
        Ensure superuser can get all user objects.
        """
        url = reverse('user-list')
        self.set_basic_authentication(is_admin=True)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_my_user(self):
        """
        Ensure user can get own user object.
        """
        url = reverse('user-list')
        user = self.set_basic_authentication(is_admin=False)
        user_url = f'{url}{user.id}/'
        response = self.client.get(user_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], user.id)

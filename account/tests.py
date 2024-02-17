# from rest_framework.test import APITestCase
# from django.urls import reverse
# from account.models import User

# class AutoApiTestCase(APITestCase):
#     def test_get(self):
#         user_1 = User.objects.create(email='user1@gmail.com', name='user1')
#         user_2 = User.objects.create(email='user2@gmail.com', name='user2')
    
#         url = 'api/v1/account/register/'
#         # print(url)
#         print('-------------')
#         response = self.client.get(url)
#         # print(response.content)

# from django.test import TestCase

from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from django.contrib.auth import get_user_model
from .views import *
from django.contrib.auth.hashers import make_password


User = get_user_model()

class AuthTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='user@gmail.com',
            password='12345678',
            is_active=True,
            activation_code='1234'
        )
    
    def test_registration(self):
        data = {
            'email': 'new_test_user@gmail.com',
            'password': '12345678',
            'password_confirm': '12345678',
            'name': 'test'
        }

        request = self.factory.post('api/v1/account/register/', data, format='json')
        print(request)
        print('===========')
        view = RegistrationView.as_view()
        response = view(request)
        print(response)
        print('===========')
        assert User.objects.filter(email=data['email']).exists()
        # assert response.status_code == 201


    def test_login(self):
        data = {
            'email': 'user@gmail.com',
            'password': '12345678'
        }
        request = self.factory.post('login/', data, format='json')
        view = LoginView.as_view()
        response = view(request)
        assert 'token' in response.data

    def test_logout(self):
        data = {
            'email': 'user@gmail.com',
            'password': '12345678'
        }
        request = self.factory.post('logout/', data, format='json')
        view = LogoutView.as_view()
        response = view(request)
        assert User.objects.filter(email=data['email']).delete()

    def test_change_password(self):
        data = {
            'old_password': '12345678',
            'new_password': '1234567a',
            'new_password_confirm': '1234567a'
        }
        request = self.factory.post('change_password', data, format='json')
        force_authenticate(request, user=self.user)
        view = ChangePasswordView.as_view()
        response = view(request)
        assert response.status_code == 200


    def test_forgot_password(self):
        request = self.factory.post('forgot-password/', data = {'email': 'user@gmail.com'}, format='json')
        view = ForgotPasswordView.as_view()
        response = view(request)
        assert response.status_code == 200

    def test_forgot_pass_complete(self):
        data = {
                'email': 'user@gmail.com', 
                'code': '1234', 
                'password': '1234test', 
                'password_confirm': '1234test'
                }
        request = self.factory.post('forgot-password-complete/', data, format='json')
        view = ForgotPasswordCompleteView.as_view()
        response = view(request)
        print(response.data)
        assert response.status_code == 200


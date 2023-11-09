from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser


class CustomUserTestCase(APITestCase):

    def setUp(self):
        data_user = {'email': 'test@mail.com', 'password': 123, 'phone_number': '+79998336868', 'is_staff': True}
        self.test_user = CustomUser.objects.create(**data_user)
        self.client.force_authenticate(user=self.test_user)

    def test_retrieve_user(self):
        response = self.client.get(reverse('users:users-detail', kwargs={'pk': self.test_user.pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['id'], self.test_user.pk)
        self.assertEquals(response.json()['email'], self.test_user.email)
        self.assertEquals(response.json()['phone_number'], self.test_user.phone_number)

    def test_create_user(self):
        user_data = {'email': 'test_create@mail.com', 'password': 'qweasd123qwe', 'phone_number': '+79998336868'}
        response = self.client.post(reverse('users:users-list'), data=user_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json()['email'], user_data['email'])
        self.assertEquals(response.json()['phone_number'], user_data['phone_number'])
        user = CustomUser.objects.get(email=response.json()['email'])
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_staff, False)

    def test_create_user_wrong_email(self):
        user_data = {'email': 'wrong.com', 'password': 'qweasd123qwe', 'phone_number': '+79998336868'}
        response = self.client.post(reverse('users:users-list'), data=user_data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json()['email'], ['Enter a valid email address.'])
        valid_data = user_data.copy()
        valid_data['email'] = 'valid@email.com'
        response = self.client.post('http://localhost:8000/users/', data=valid_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_invalid_phone(self):
        user_data = {'email': 'test_invalid@email.com', 'password': 'qweasd123qwe', 'phone_number': '9998336868'}
        response = self.client.post(reverse('users:users-list'), data=user_data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json()['phone_number'], ['The phone number entered is not valid.'])
        valid_data = user_data.copy()
        valid_data['phone_number'] = '+905345250000'
        response = self.client.post('http://localhost:8000/users/', data=valid_data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        user_data = {'email': 'test_two@mail.com', 'password': 'qweasd123qwe', 'phone_number': '+79998336868'}
        self.client.post(reverse('users:users-list'), data=user_data)
        response_get = self.client.get(reverse('users:users-list'))
        self.assertEquals(response_get.status_code, status.HTTP_200_OK)
        self.assertEquals(CustomUser.objects.all().count(), 2)
        self.assertEquals(response_get.json()['results'][0]['email'], self.test_user.email)
        self.assertEquals(response_get.json()['results'][1]['email'], user_data['email'])

    def test_patch_users(self):
        user_data = {'email': 'updated@mail.com'}
        response = self.client.patch(
            reverse('users:users-detail', kwargs={'pk': self.test_user.pk}), data=user_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['email'], 'updated@mail.com')

    def test_put_user(self):
        user_data = {
            'email': 'updated@mail.com', 'phone_number': '+905335250000', 'is_active': False, 'is_staff': False}
        response = self.client.patch(
            reverse('users:users-detail', kwargs={'pk': self.test_user.pk}), data=user_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['email'], 'updated@mail.com')
        self.assertEquals(response.json()['is_active'], False)

    def test_delete_user(self):
        response = self.client.delete(reverse('users:users-detail', kwargs={'pk': self.test_user.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(CustomUser.objects.all().count(), 0)

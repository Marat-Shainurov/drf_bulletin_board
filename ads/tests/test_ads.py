from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ads.models import Ad
from users.models import CustomUser


class AdsTestCase(APITestCase):

    def setUp(self) -> None:
        data_user = {'email': 'test@mail.com', 'password': 123, 'phone_number': '+79998336868', 'is_staff': True}
        self.test_user = CustomUser.objects.create(**data_user)
        self.client.force_authenticate(user=self.test_user)
        data_ad = {"title": "Test ad", "price": 1000, "description": "Test ad description", 'author': self.test_user}
        self.test_ad = Ad.objects.create(**data_ad)

    def test_create_ad(self):
        data = {"title": "Create ad", "price": 1500, "description": "Creation test"}
        response = self.client.post(reverse('ads:ads_create'), data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json()['title'], data['title'])
        self.assertEquals(eval(response.json()['price']), data['price'])
        self.assertEquals(response.json()['description'], data['description'])

    def test_ads_list(self):
        response = self.client.get(reverse('ads:ads_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['results'][0]['id'], self.test_ad.pk)
        self.assertEquals(response.json()['results'][0]['title'], self.test_ad.title)
        self.assertEquals(
            response.json()['results'][0]['author'],
            {'id': self.test_user.pk, 'email': self.test_user.email, 'phone_number': self.test_user.phone_number})
        self.assertEquals(response.json()['results'][0]['ad_reviews'], [])

    def test_get_ad(self):
        response = self.client.get(reverse('ads:ads_get', kwargs={'pk': self.test_ad.pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['id'], self.test_ad.pk)
        self.assertEquals(response.json()['description'], self.test_ad.description)
        self.assertEquals(response.json()['preview'], None)
        self.assertEquals(
            response.json()['author'],
            {'id': self.test_user.pk, 'email': self.test_user.email, 'phone_number': self.test_user.phone_number})

    def test_get_ad_not_owner(self):
        data_user = {'email': 'test2@mail.com', 'password': 123, 'phone_number': '+79998336867', 'is_staff': False}
        new_user = CustomUser.objects.create(**data_user)
        self.client.force_authenticate(user=new_user)
        response = self.client.get(reverse('ads:ads_get', kwargs={'pk': self.test_ad.pk}))
        self.assertEquals(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEquals(response.json()['detail'], 'You do not have permission to perform this action.')

    def test_get_ad_not_owner_admin(self):
        data_user = {'email': 'test2@mail.com', 'password': 123, 'phone_number': '+79998336867', 'is_staff': True}
        new_user = CustomUser.objects.create(**data_user)
        self.client.force_authenticate(user=new_user)
        response = self.client.get(reverse('ads:ads_get', kwargs={'pk': self.test_ad.pk}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['id'], self.test_ad.pk)

    def test_get_ad_with_reviews(self):
        review_1 = {"text": "Review one", "ad": self.test_ad.pk, 'author': self.test_user}
        review_2 = {"text": "Review two", "ad": self.test_ad.pk, 'author': self.test_user}
        self.test_ad.ad_reviews.create(**review_1)
        self.test_ad.ad_reviews.create(**review_2)
        response = self.client.get(reverse('ads:ads_get', kwargs={'pk': self.test_ad.pk}))
        self.assertIsInstance(response.json()['ad_reviews'], list)
        self.assertEquals(len(response.json()['ad_reviews']), 2)
        self.assertEquals(response.json()['ad_reviews'][0]['text'], review_1['text'])
        self.assertEquals(response.json()['ad_reviews'][1]['text'], review_2['text'])

    def test_update_ad(self):
        data_to_update = {"title": "Updated", "price": 2000, "description": "updated description"}
        response = self.client.put(reverse('ads:ads_update', kwargs={'pk': self.test_ad.pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['title'], data_to_update['title'])
        self.assertEquals(response.json()['description'], data_to_update['description'])
        self.assertEquals(eval(response.json()['price']), data_to_update['price'])

    def test_update_ad_field_missing(self):
        data_to_update = {"title": "Updated", "description": "updated description"}
        response = self.client.put(reverse('ads:ads_update', kwargs={'pk': self.test_ad.pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.json()['price'], ['This field is required.'])

    def test_partial_update_ad(self):
        data_to_update = {"title": "Updated"}
        response = self.client.patch(reverse('ads:ads_update', kwargs={'pk': self.test_ad.pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['title'], data_to_update['title'])

    def test_delete_ad(self):
        response = self.client.delete(reverse('ads:ads_delete', kwargs={'pk': self.test_ad.pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

# todo:
#  Add password_reset
#  Add dockerfiles.
#  Add readme file

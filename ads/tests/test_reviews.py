from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ads.models import Ad
from users.models import CustomUser


class ReviewTestCase(APITestCase):

    def setUp(self) -> None:
        data_user = {'email': 'test@mail.com', 'password': 123, 'phone_number': '+79998336868', 'is_staff': True}
        self.test_user = CustomUser.objects.create(**data_user)
        self.client.force_authenticate(user=self.test_user)
        data_ad = {"title": "Test ad", "price": 1000, "description": "Test ad description", 'author': self.test_user}
        self.test_ad = Ad.objects.create(**data_ad)
        data_test_review = {"text": "Review one", "ad": self.test_ad.pk, 'author': self.test_user}
        self.test_ad.ad_reviews.create(**data_test_review)

    def test_create_review(self):
        data_review = {"text": "Create review", "ad": self.test_ad.pk}
        response = self.client.post(reverse('ads:reviews_create'), data=data_review)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.json()['text'], data_review['text'])
        self.assertEquals(response.json()['ad'], data_review['ad'])

    def test_get_reviews_list(self):
        response = self.client.get(reverse('ads:reviews_list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json()['results'], list)
        self.assertEquals(len(response.json()['results']), 1)
        self.assertEquals(response.json()['results'][0]['id'], self.test_ad.ad_reviews.first().pk)
        self.assertEquals(response.json()['results'][0]['text'], self.test_ad.ad_reviews.first().text)

    def test_get_review(self):
        response = self.client.get(
            reverse('ads:reviews_get', kwargs={'pk': self.test_ad.ad_reviews.first().pk}))
        self.assertEquals(response.json()['id'], self.test_ad.ad_reviews.first().pk)
        self.assertEquals(response.json()['text'], self.test_ad.ad_reviews.first().text)
        self.assertEquals(response.json()['ad'], self.test_ad.pk)

    def test_update_review(self):
        data_to_update = {'text': 'Updated text', 'ad': self.test_ad.pk}
        response = self.client.put(
            reverse('ads:reviews_update',
                    kwargs={'pk': self.test_ad.ad_reviews.first().pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['text'], data_to_update['text'])

    def test_partial_update_review(self):
        data_to_update = {'text': 'Updated text'}
        response = self.client.patch(
            reverse('ads:reviews_update',
                    kwargs={'pk': self.test_ad.ad_reviews.first().pk}), data=data_to_update)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.json()['text'], data_to_update['text'])

    def test_delete_review(self):
        response = self.client.delete(
            reverse('ads:reviews_delete', kwargs={'pk': self.test_ad.ad_reviews.first().pk}))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

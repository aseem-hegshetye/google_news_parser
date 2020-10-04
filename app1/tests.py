from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app1.models import *


class TestGetNewsAPIView(APITestCase):

    def test_get_request(self):
        response = self.client.get(path=reverse('app1:api:get_news'))
        self.assertURLEqual(response.status_code, status.HTTP_200_OK)

    def test_news_model(self):
        """
        on successful get request, we should have
        some transactions in News model
        """
        response = self.client.get(path=reverse('app1:api:get_news'))
        no_of_objs = News.objects.count()
        self.assertTrue(no_of_objs > 0)

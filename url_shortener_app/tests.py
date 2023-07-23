from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Url


class UrlAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_add_long_url(self):
        url_data = {
            "long_url": "https://example.com/very/long/url"
        }
        response = self.client.post(reverse("add-long-url"), data=url_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Url.objects.count(), 1)

    def test_get_short_url(self):
        url = Url.objects.create(long_url="https://example.com/another/long/url")
        response = self.client.get(reverse("get-short-url"), {"short_url": url.short_url})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["long_url"], url.long_url)

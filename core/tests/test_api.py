from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Triange


class TriangleTest(APITestCase):
    def test_when_triangle_is_scalene(self):
        url = reverse("triangle-list")
        data = {"side_one": 3, "side_three": 2, "side_two": 5}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Triange.objects.count(), 1)
        self.assertIn(response.data, "Scalene")

    def test_when_triangle_is_equilateral(self):
        url = reverse("triangle-list")
        data = {"side_one": 3, "side_three": 3, "side_two": 3}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Triange.objects.count(), 1)
        self.assertIn(response.data, "Equilateral")

    def test_when_triangle_is_isosceles(self):
        url = reverse("triangle-list")
        data = {"side_one": 3, "side_three": 3, "side_two": 6}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Triange.objects.count(), 1)
        self.assertIn(response.data, "Isosceles")

    def test_when_data_its_not_a_triangle(self):
        url = reverse("triangle-list")
        data = {"side_one": 1, "side_two": 1, "side_three": 5}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data, "It seems that it's not a triangle")

    def test_when_one_size_is_zero(self):
        url = reverse("triangle-list")
        data = {"side_one": 1, "side_two": 1, "side_three": 0}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data, "It seems that it's not a triangle")

    def test_with_invalid_data(self):
        url = reverse("triangle-list")
        data = {"side_one": 3, "side_two": 3, "side_three": "X"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data, "Please enter a valid number")

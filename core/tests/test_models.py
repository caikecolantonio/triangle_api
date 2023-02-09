from django.test import TestCase
import pytest
from core.models import Triange, TriangleType
from django.db import IntegrityError


class TriangleTest(TestCase):
    def test_create_triangle_equilateral(self):
        triangle = Triange.objects.create(
            side_one=5,
            side_two=5,
            side_three=5,
            triangle_type=TriangleType.EQUILATERAL.value,
        )

        self.assertEqual(triangle.side_one, 5)
        self.assertEqual(triangle.side_two, 5)
        self.assertEqual(triangle.side_three, 5)
        self.assertEqual(triangle.triangle_type, TriangleType.EQUILATERAL.value)

    def test_create_triangle_isosceles(self):
        triangle = Triange.objects.create(
            side_one=3,
            side_two=3,
            side_three=6,
            triangle_type=TriangleType.ISOSCELES.value,
        )

        self.assertEqual(triangle.side_one, 3)
        self.assertEqual(triangle.side_two, 3)
        self.assertEqual(triangle.side_three, 6)
        self.assertEqual(triangle.triangle_type, TriangleType.ISOSCELES.value)

    def test_create_triangle_scalene(self):
        triangle = Triange.objects.create(
            side_one=3,
            side_two=2,
            side_three=5,
            triangle_type=TriangleType.SCALENE.value,
        )

        self.assertEqual(triangle.side_one, 3)
        self.assertEqual(triangle.side_two, 2)
        self.assertEqual(triangle.side_three, 5)
        self.assertEqual(triangle.triangle_type, TriangleType.SCALENE.value)

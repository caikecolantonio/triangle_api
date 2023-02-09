from django.db import models
from django.utils.translation import gettext_lazy as _


class TriangleType(models.TextChoices):
    EQUILATERAL = ("Equilateral",)
    ISOSCELES = ("Isosceles",)
    SCALENE = ("Scalene",)


class Triange(models.Model):
    side_one = models.IntegerField()
    side_two = models.IntegerField()
    side_three = models.IntegerField()
    triangle_type = models.CharField(
        blank=True, choices=TriangleType.choices, max_length=11
    )

from core.models import Triange
from rest_framework import serializers


class TriangleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triange
        fields = ("side_one", "side_two", "side_three", "triangle_type")

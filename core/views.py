from rest_framework import viewsets
from rest_framework import permissions
from core.models import Triange, TriangleType
from core.serializer import TriangleSerializer
from rest_framework.response import Response


class TriangleViewSet(viewsets.ModelViewSet):
    queryset = Triange.objects.get_queryset().order_by("id")
    serializer_class = TriangleSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = {
                "side_one": int(request.data.get("side_one")),
                "side_two": int(request.data.get("side_two")),
                "side_three": int(request.data.get("side_three")),
            }
        except ValueError:
            return Response("Please enter a valid number", status=400)

        not_triangle = "It seems that it's not a triangle"
        if data["side_one"] == 0 or data["side_two"] == 0 or data["side_three"] == 0:
            return Response(not_triangle, status=400)
        if (
            data["side_one"] + data["side_two"] < data["side_three"]
            or data["side_one"] + data["side_three"] < data["side_two"]
            or data["side_two"] + data["side_three"] < data["side_one"]
        ):
            return Response(not_triangle, status=400)

        # _Check for equilateral triangle
        if data["side_one"] == data["side_two"] == data["side_three"]:
            data["triangle_type"] = TriangleType.EQUILATERAL.value
            triangle_type = TriangleType.EQUILATERAL.label

        # Check for isosceles triangle
        elif (
            data["side_one"] == data["side_two"]
            or data["side_two"] == data["side_three"]
            or data["side_three"] == data["side_one"]
        ):
            data["triangle_type"] = TriangleType.ISOSCELES.value
            triangle_type = TriangleType.ISOSCELES.label
        # Otherwise scalene triangle
        else:
            data["triangle_type"] = TriangleType.SCALENE.value
            triangle_type = TriangleType.SCALENE.label

        Triange.objects.create(**data)
        return Response(triangle_type, status=201)

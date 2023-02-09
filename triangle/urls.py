from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, permissions
from core.views import TriangleViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "triangle"

router = routers.DefaultRouter()
router.register(r"triangle", TriangleViewSet, "triangle")

schema_view = get_schema_view(
    openapi.Info(
        title="Triangle API",
        default_version="v1",
        description="All endpoints documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("", include("rest_framework.urls", namespace="rest_framework")),
    path("doc/", schema_view.with_ui("swagger", cache_timeout=0), name="doc"),
]

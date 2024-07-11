from django.conf import settings
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title=settings.SWAGGER_TITLE,
        default_version='v1',
        description=settings.SWAGGER_DESCRIPTION,
        contact=openapi.Contact(email=settings.SWAGGER_EMAIL),
        license=openapi.License(name=settings.SWAGGER_LICENSE),
    ),
    urlconf='backend.api.v1.urls',
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('testing/', TestAPIView.as_view())
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='v1-schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='v1-schema-redoc'),
]

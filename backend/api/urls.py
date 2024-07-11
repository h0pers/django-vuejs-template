from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title=settings.SWAGGER_TITLE,
        default_version=settings.SWAGGER_DEFAULT_API_VERSION,
        description=settings.SWAGGER_DESCRIPTION,
        contact=openapi.Contact(email=settings.SWAGGER_EMAIL),
        license=openapi.License(name=settings.SWAGGER_LICENSE),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('v1/', include(('backend.api.v1.urls', 'v1'))),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
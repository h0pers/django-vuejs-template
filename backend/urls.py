from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include


class FrontendView(TemplateView):
    template_name = 'dist/index.html'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FrontendView.as_view()),
    path('api/', include(('backend.api.urls', 'api'))),
]

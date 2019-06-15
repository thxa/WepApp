from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/v1/', include('backend.main.urls')),
    path('api/auth/', include('backend.account.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', index_view),
]

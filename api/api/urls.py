from django.contrib import admin
from django.urls import path, include
# from main.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    path('api/auth/', include('account.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', IndexView.as_view()),
    # path('create/', VideoCreate.as_view())
]

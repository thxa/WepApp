from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserListAPIView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetileAPIView.as_view(), name='user')
]

urlpatterns = format_suffix_patterns(urlpatterns)


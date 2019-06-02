from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    # path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', views.SignUp.as_view(), name="signup"),
    # path('login/', views.LoginAPIView.as_view(), name="login"),
    path('login/', obtain_auth_token, name="login")
    # path('users/', views.UserListAPIView.as_view(), name='users'),
    # path('users/<int:pk>/', views.UserDetileAPIView.as_view(), name='user')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)


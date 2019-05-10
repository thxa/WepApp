"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('h/', views.hello_web, name='hello'),
    # path('hello/', views.HelloAPIView.as_view(), name="test"),

    path('videos/', views.VideoListAPIView.as_view(), name='videos'),
    path('videos/<slug>/', views.VideoDetileAPIView.as_view(), name='video'),

    path('categories/', views.CategoryListAPIView.as_view(), name='categories'),
    path('categories/<slug>/', views.CategoryDetileAPIView.as_view(), name='category'),

    path('seasones/', views.SeasonListAPIView.as_view(), name='seasones'),
    path('seasones/<slug>/', views.SeasonDetileAPIView.as_view(), name='season'),
]

urlpatterns = format_suffix_patterns(urlpatterns)



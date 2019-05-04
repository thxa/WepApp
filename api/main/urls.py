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
    path('h/', views.hello_web),
    path('videos/', views.VideoListAPIView.as_view()),
    path('videos/<slug>/', views.VideoDetileAPIView.as_view()),
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<slug>/', views.CategoryDetileAPIView.as_view()),
    path('seasones/', views.SeasonListAPIView.as_view()),
    path('seasones/<slug>/', views.SeasonDetileAPIView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)

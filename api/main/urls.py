from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'seasones', views.SeasonViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('schema/', schema_view),
    # path('search/', views.SearchListView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)



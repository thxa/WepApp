# From rest framework
from rest_framework import permissions, viewsets

# From Main App
from .models import Video, Category, Season
from .serializers import SeasonSerializer, CategorySerializer, VideoSerializer
from .permissions import IsOwnerOrReadOnly


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    lookup_field = 'slug'
    serializer_class = SeasonSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    allowed_methods = ('GET', 'OPTIONS', 'HEAD')
    lookup_field = 'slug'
    serializer_class = CategorySerializer
    # permission_classes = (permissions.IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save()


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    lookup_field = 'slug'
    serializer_class = VideoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # # def video(self, request, *args, **kwargs):
    # #     video = self.get_object()
    # #     return Response(video)


# class SearchListView(generics.ListAPIView):
#     serializer_class = SeasonSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     queryset = Season.objects.all()
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('name',)

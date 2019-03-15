from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from main.models import Video, Category, Season
from main import serializers
from django.shortcuts import get_object_or_404
from django.views import View
# Create your views here.

@api_view(['GET'])
def hello_web(request):
    """
     Test api .
    """
    if request.method == 'GET':
        data = {'content': 'hello web'}

        return Response(data)

    # elif request.method == 'POST':
    # #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoListAPIView(APIView):
    '''  This is Video List API View   '''
    serializer_class = serializers.VideoSerializer

    def get(self, request ,format=None):
        videos = Video.objects.all()
        serializer = serializers.VideoSerializer(videos, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = serializers.VideoSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoDetileAPIView(APIView):
    ''' This is Video Detile API View  '''
    serializer_class = serializers.VideoSerializer

    def get(self, request, slug, format=None):
        video = get_object_or_404(Video, slug=slug)
        serializer = serializers.VideoSerializer(video)
        return Response(serializer.data)

    # def post(self, request, format=None):pass

    def put(self, request, slug, format=None):
        video = get_object_or_404(Video, slug=slug)
        serializer = serializers.VideoSerializer(video, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        video = get_object_or_404(Video, slug=slug)
        serializer = serializers.VideoSerializer(video, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, slug, format=None):
        video = get_object_or_404(Video, slug=slug)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryListAPIView(APIView):
    '''  This is Category List API View   '''
    serializer_class = serializers.CategorySerializer

    def get(self, request ,format=None):
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CategorySerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetileAPIView(APIView):
    ''' This is Category Detile API View  '''
    serializer_class = serializers.CategorySerializer

    def get(self, request, slug, format=None):
        category = get_object_or_404(Category, slug=slug)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)

    # def post(self, request, format=None):pass

    def put(self, request, slug, format=None):
        category = get_object_or_404(Category, slug=slug)
        serializer = serializers.CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, slug, format=None):
        category = get_object_or_404(Category, slug=slug)
        serializer = serializers.CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        category = get_object_or_404(Category, slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class SeasonListAPIView(APIView):
    '''  This is Season List API View   '''
    serializer_class = serializers.SeasonSerializer

    def get(self, request ,format=None):
        seasones = Season.objects.all()
        serializer = serializers.SeasonSerializer(seasones, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.SeasonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeasonDetileAPIView(APIView):
    ''' This is Season Detile API View  '''
    serializer_class = serializers.SeasonSerializer

    def get(self, request, slug, format=None):
        season = get_object_or_404(Season, slug=slug)
        serializer = serializers.SeasonSerializer(season)
        # season.get_next_in_order()
        # serializer.data += {"next": season.video.get_next_in_order()}
        return Response(serializer.data)

    # def post(self, request, format=None):pass

    def put(self, request, slug, format=None):
        season = get_object_or_404(Season, slug=slug)
        serializer = serializers.CategorySerializer(season, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, slug, format=None):
        season = get_object_or_404(Season, slug=slug)
        serializer = serializers.SeasonSerializer(season, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, format=None):
        season = get_object_or_404(Season, slug=slug)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name, context=None)

class VideoCreate(View):
    template_name = 'main/create_video.html'

    def get(self, request):
        return render(request, self.template_name, context=None)

# @api_view(['GET', 'PUT', 'PATCH','DELETE'])
# def video_detile(request, slug):
#     """
#      video detile api .
#     """
#     video = get_object_or_404(Video, slug=slug)
#     if request.method == 'GET':

#         serializer = serializers.VideoSerializer(video)
#         return Response(serializer.data)

#     elif request.method == 'PUT':

#         serializer = serializers.VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'PATCH':

#         serializer = serializers.VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         video.delete()
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)






# @api_view(['GET', 'POST'])
# def video_list(request):
#     """
#      video list api .
#     """
#     if request.method == 'GET':
#         videos = Video.objects.all()
#         serializer = serializers.VideoSerializer(videos, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = serializers.VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

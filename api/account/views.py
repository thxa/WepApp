from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

from . import serializers


class UserListAPIView(APIView):
    '''  This is User List API View   '''
    serializer_class = serializers.UserSerializer

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetileAPIView(APIView):
    ''' This is User Detile API View  '''
    serializer_class = serializers.UserSerializer

    def get(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

    # def post(self, request, format=None):pass

    def put(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = serializers.UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        serializer = serializers.UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

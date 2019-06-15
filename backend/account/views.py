from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny

from . import serializers
# from .models import Profile

# allowed_methods = ("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD")


class APIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'signup': reverse('login', request=request, format=format),
            'login': reverse('signup', request=request, format=format)
        })


class SignUp(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            return Response({'token': user.auth_token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
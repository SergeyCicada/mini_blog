from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserCreateSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

from django.contrib.auth.models import User, Group

from rest_framework import viewsets

from quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.auth import JWTAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [JWTAuthentication]

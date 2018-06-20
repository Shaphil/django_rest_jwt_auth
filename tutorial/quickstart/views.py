import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group

from rest_framework import views, viewsets
from rest_framework.response import Response

from quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.auth import JWTAuthentication, Utilities


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # authentication_classes = [JWTAuthentication]


class LoginView(views.APIView):
    def post(self, request):
        utils = Utilities()
        username = request.data['username']
        password = request.data['password']

        print('__LOG__', username, password)

        # https://docs.djangoproject.com/en/2.0/topics/auth/default/#authenticating-users
        user = authenticate(username=username, password=password)

        if user:
            token = utils.encode(request)
            return Response(
                json.dumps({'access_token': token}),
                status=200
            )
        else:
            return Response(
                json.dumps({'error': 'Invalid username/password'}),
                status=400
            )

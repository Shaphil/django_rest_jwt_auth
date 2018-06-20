import jwt

from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed

from tutorial.settings import SECRET_KEY

ALGORITHM = 'HS256'

# custom authentication: http://www.django-rest-framework.org/api-guide/authentication/#custom-authentication


class JWTAuthentication(BaseAuthentication):
    # override authenticate() method
    def authenticate(self, request):
        # get header info
        header = get_authorization_header(request)
        if header is None:
            return None

        # auth info will be two space separated values
        # eg. bearer cnso9iduh0297wbeib
        auth = header.split()
        if len(auth) != 2:
            raise AuthenticationFailed(
                'Auth header must contain 2 values separated by space'
            )

        # the second part of the auth string is the token
        token = auth[1]
        return self.get_user(token), None

    def get_user(self, token):
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = data['id']
        email = data['email']
        user = User.objects.get(pk=user_id)
        test_token = Utilities().encode_user(user)

        print('__LOG__', token)
        print('__LOG__', test_token)

        if test_token != token.decode('utf-8'):
            raise AuthenticationFailed('Token mismatch, authentication failed')

        return (user, token)


class Utilities:
    def encode(self, request):
        user = self.get_user_from_request(request)
        token = self.encode_user(user)

        return token

    def encode_user(self, user):
        data = {'id': user.id, 'email': user.email}

        return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM).decode('utf-8')

    def get_user_from_request(self, request):
        username = request.data['username']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExits:
            raise AuthenticationFailed('Invalid Username/Password')

        return user

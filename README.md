# django_rest_jwt_auth
Custom authentication based on JWT applied on the top of the quickstart found on Django REST Framework - http://www.django-rest-framework.org/tutorial/quickstart/

# Running the server
* You may want to work with a virtualenv.
* Install dependencies: `pip install -r requirements.txt`
* CD to `tutorial` directory and apply migrations: `python manage.py migrate`
* Create a superuser `python manage.py createsuperuser`
* Run: `python manage.py runserver`

The server should be available at port 8000 of your localhost. Go to http://localhost:8000/ and check if it worked.

# Usage example
There are two resources. 

"users": "http://localhost:8000/users/",

"groups": "http://localhost:8000/groups/"

"groups" is open to requests but "users" is protected. To view users, you'll need to authenticate. 

Send a POST request to http://localhost:8000/auth/ with the following data
```
{
    "username": your super user's username,
    "password": your super user's password
}
```

and you should receive an `access_token`. Each time you send a request to "users" endpoint, you'll need that token.

# Resources
* http://www.django-rest-framework.org/api-guide/authentication/#custom-authentication
* https://github.com/davesque/django-rest-framework-simplejwt
* https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332

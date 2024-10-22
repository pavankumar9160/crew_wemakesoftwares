from django.db import models

# Create your models here.

from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# # Custom user manager
# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)


# # Custom user model
# class User(AbstractBaseUser, PermissionsMixin):
#     firstname = models.CharField(max_length=50, null=True, blank=True)
#     lastname = models.CharField(max_length=50, null=True, blank=True)
#     email = models.EmailField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     phonenumber = models.CharField(max_length=10, null=True, blank=True)
    
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['firstname', 'lastname']

#     objects = UserManager()  # Assign the custom manager

#     def __str__(self):
#         return self.email


class User(models.Model):
    firstname = models.CharField(max_length=50, null=True, blank=True)
    lastname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=10, null=True, blank=True)
    

    def __str__(self):
        return self.email


from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500,default="NA")
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1) 

    def __str__(self):
        return self.title

    




    
    

from rest_framework import serializers
from .models import *
# from django.contrib.auth import authenticate

# class Signupserializer(serializers.ModelSerializer):
    
#     firstname = serializers.CharField(required =False)
#     lastname = serializers.CharField(required =False)
#     email = serializers.EmailField(required =False)
#     password = serializers.CharField(required =False)
#     password2 = serializers.CharField(required = False)
#     phonenumber = serializers.CharField(required =False)
    
#     def validate(self, data):
#         if data.get('password') != data.get('password2'):
#             raise serializers.ValidationError({'password': 'Passwords must match.'})
#         return data
    
    
#     class Meta:
#         model = User
#         fields = "__all__"
        
#     def create(self,validated_data):
#         requested_data = User.objects.create(
#       firstname =   validated_data.get('firstname'),
#       lastname =   validated_data.get('lastname'),
#       email = validated_data.get('email'),
#       password = validated_data.get('password'),
#       phonenumber = validated_data.get('phonenumber'),
      
    
      
#     )
#         return requested_data
    


# class LoginSerializer(serializers.Serializer):
#    email = serializers.CharField()
#    password = serializers.CharField()

#    def validate(self, data):
#        user = authenticate(**data)
#        if user is None:
#            raise serializers.ValidationError('Invalid credentials')
#        return {'user': user}
    
    
# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ['id', 'title','user'] 


          
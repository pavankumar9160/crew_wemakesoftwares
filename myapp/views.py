from django.shortcuts import render
# from rest_framework import status, generics

# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken 

# from .serializers import  Signupserializer,LoginSerializer 

# # Create your views here.

# class Signupview(generics.CreateAPIView):
    
#     serializer_class = Signupserializer
#     permission_classes = [AllowAny]
#     authentication_classes = [] 
#     def post(self,request):
#         serializer =   self.get_serializer(data =request.data,context ={'request':request})
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'user': Signupserializer(user).data,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.permissions import IsAuthenticated

# class LoginView(generics.GenericAPIView):
    
#     serializer_class = LoginSerializer
   
    

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
        
#         if serializer.is_valid():
#             # Extract user from validated data
#             user = serializer.validated_data['user']
            
#             # Create JWT tokens
#             refresh = RefreshToken.for_user(user)
            
#             # Create response object
#             response = Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
            
#             # Set tokens in cookies
#             response.set_cookie('access', str(refresh.access_token), httponly=True, samesite='Strict')
#             response.set_cookie('refresh', str(refresh), httponly=True, samesite='Strict')
            
#             return response
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
def signup_page(request):

    return render(request,'signup.html')

def login_page(request):

    return render(request,'login.html')    

def todo_page(request):
    return render(request,'todo.html')
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate, login
import json

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            email = data.get('email')
            password = data.get('password')
            password2 = data.get('password2')
            phonenumber = data.get('phonenumber')

            # Check if passwords match
            if password != password2:
                return JsonResponse({"password2": ["Passwords do not match."]}, status=400)

            # Check if user already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse({"email": ["Email already in use."]}, status=400)

            # Create a new user
            user = User.objects.create_user(
                username=email,
                email=email,
                first_name=firstname,
                last_name=lastname,
                password=password,
            )


            return JsonResponse({"message": "User registered successfully!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid data format."}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=405)


from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.middleware.csrf import get_token

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            csrf_token = get_token(request)  # Get CSRF token for the session
            return JsonResponse({
                'message': 'Login successful',
                'csrf_token': csrf_token
            })
        else:
            return JsonResponse({
                'error': 'Invalid credentials'
            }, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

from django.shortcuts import redirect
from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('login_page') 










from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import TodoList
from django.views.decorators.csrf import csrf_exempt


@login_required
def todo_list(request):
    if request.method == 'GET':
        todos = TodoList.objects.filter(user=request.user)
        return render(request, 'todo.html', {'todos': todos})

    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
           
            todo = TodoList.objects.create(user=request.user, title=title, description=description)
            return JsonResponse({'id': todo.id, 'title': todo.title, 'description': todo.description}, status=201)
        return JsonResponse({'error': 'Title and description are required'}, status=400)

@login_required
def fetch_todos(request):
    if request.method == 'GET':
     
        todos = TodoList.objects.filter(user=request.user)
       
        todos_data = [{'id': todo.id, 'title': todo.title, 'description': todo.description} for todo in todos]
        return JsonResponse(todos_data, safe=False)

@login_required
def update_todo(request, pk):
    if request.method == 'POST':  
        try:
            todo = TodoList.objects.get(pk=pk, user=request.user)
        except TodoList.DoesNotExist:
            return JsonResponse({'detail': 'Todo not found or not accessible.'}, status=404)

        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
           
            todo.title = title
            todo.description = description
            todo.save()
            return JsonResponse({'id': todo.id, 'title': todo.title, 'description': todo.description}, status=200)
        return JsonResponse({'error': 'Title and description are required'}, status=400)

@login_required
def delete_todo(request, pk):
    try:
        todo = TodoList.objects.get(pk=pk, user=request.user)
    except TodoList.DoesNotExist:
        return JsonResponse({'detail': 'Todo not found or not accessible.'}, status=404)

    todo.delete()
    return JsonResponse({'detail': 'Todo deleted successfully!'}, status=204)

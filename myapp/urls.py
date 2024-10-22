
from django.urls import path,include
from . import views
# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
     path('signup_api/',views.signup_view,name="signup_api"),
     path("signup/",views.signup_page,name="signup"),
     path('login_page/',views.login_page,name="login_page"),
     path('login/',views.login_view,name="login"),
     path('todo_page/',views.todo_page, name="todo_page"),
     path('todos/', views.todo_list, name='todo_list'),  
    path('', views.logout_view, name='logout'),
    path('todos/fetch/', views.fetch_todos, name='fetch_todos'),

    path('todos/update/<int:pk>/', views.update_todo, name='update_todo'), 
    path('todos/delete/<int:pk>/', views.delete_todo, name='delete_todo'),
]

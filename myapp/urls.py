"""
URL configuration for ifinance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

  path('signup_api/',views.signup_view,name="signup_api"),
  path("",views.signup_page,name="signup"),
  path('login_page/',views.login_page,name="login_page"),
  path('login/',views.login_view,name="login"),
  path('logout/', views.logout_view, name='logout'),
  path('chat_page_user/',views.chat_page_user, name="chat_page_user"),
  path('dashboard_user/',views.dashboard_user, name="dashboard_user"),
  path('agent_home/',views.agent_home,name='agent_home'),
  path('agent_dashboard/',views.agent_dashboard, name="agent_dashboard"),
  path('agent_login/',views.agent_login,name='agent_login'),
  path('agreements_user/',views.agreements_user,name='agreements_user'),
  path('community_user/',views.community_user,name='community_user'),
  path('details_v2_user/',views.details_v2_user,name='details_v2_user'),
  path('help_supp_user/',views.help_supp_user,name='help_supp_user'),
  path('init_user/',views.init_user,name='init_user'),
  path('onlychat_agent/',views.onlychat_agent,name="onlychat_agent"),
  path('personal_details/',views.personal_details,name="personal_details"),
  path('user_auth_by_agent/',views.user_auth_by_agent,name="user_auth_by_agent"),
  path('get_users_info_and_messages/',views.get_users_info_and_messages,name="get_users_info_and_messages"),
  path('send_messages/<int:chatRequestId>', views.view_messages, name="messages"),
  path('get_registered_users_info/',views.get_registered_users_info,name="get_registered_users_info"),
   path('toggle-status/<int:user_id>/', views.toggle_status, name='toggle_status'),
   path('get_user_chat_history/<int:chatRequestId>/',views.get_user_chat_history,name='get_user_chat_history'),
   path('request_chat/', views.request_chat, name='request_chat'),
   path('chat_page_agent/<int:chatRequestId>/',views.chat_page_agent,name="chat_page_agent"),
   path('load_messages/<int:chatRequestId>/',views.load_new_messages,name="load_messages"),
   path('get-consent-form/', views.get_consent_form, name='get_consent_form'),
    path('save-consent-answers/', views.save_consent_answers, name='save_consent_answers'),
    path('update_details/',views.update_details,name='update_details'),
   


  
  
  
  
  
  
   
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
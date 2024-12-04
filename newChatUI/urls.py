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
from newChatUI import views



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
  path('send_messages/<int:chatRequestId>/', views.view_messages, name="messages"),
  path('get_registered_users_info/',views.get_registered_users_info,name="get_registered_users_info"),
   path('toggle-status/<int:user_id>/', views.toggle_status, name='toggle_status'),
   path('get_user_chat_history/<int:chatRequestId>/',views.get_user_chat_history,name='get_user_chat_history'),
   path('chat_page_user/', views.chat_page_user, name='chat_page_user'),
   path('request_chat/<int:csaId>/',views.request_chat,name="request_chat"),
   path('chat_page_agent/<int:user_id>/',views.chat_page_agent,name="chat_page_agent"),
   path('load_messages_user/<int:csaId>/',views.load_new_messages_user,name="load_messages_user"),
   path('load_messages_agent/<int:user_id>/',views.load_new_messages_agent,name="load_messages_agent"),
   path('get-consent-form/', views.get_consent_form, name='get_consent_form'),
   path('save-consent-answers/', views.save_consent_answers, name='save_consent_answers'),
   path('update_details/',views.update_details,name='update_details'),
   path('getmessages/<int:csaId>/', views.get_messages, name = "getmessages"),
   path('agent_chat_page/',views.agent_chat_page,name="agent_chat_page"),
    path('get_message_count/<int:csaId>/', views.get_message_count, name = "get_message_count"),
     path('getthe_message_count/<int:user_id>/', views.getthe_message_count, name = "get_the_message_count"),
   path('update_user_typing_status/<int:chatRequestId>/',views.update_user_typing_status, name="update_user_typing_status"),
   path('update_agent_typing_status/<int:chatRequestId>/',views.update_agent_typing_status, name="update_agent_typing_status"),
       path('get_csa_typing_status/<int:chatRequestId>/',views.get_csa_typing_status, name="get_csa_typing_status"),
path('get_user_typing_status/<int:chatRequestId>/',views.get_user_typing_status, name="get_user_typing_status"),
# path('capture-image/',views.capture_image,name="capture-image"),
path('callback_request/',views.callback_request,name="callback_request"),
 path('save-user-info/', views.save_user_info, name='save_user_info'),
  path('check-consent-status/', views.check_consent_status, name='check_consent_status'),
  path('check-profile-completion/', views.check_profile_completion, name='check_profile_completion'),
   path('start_video_recording/', views.start_video_recording, name='start_video_recording'),
    path('poll_video_recording/', views.poll_video_recording, name='poll_video_recording'),
    path('save_video/', views.save_video, name='save_video'),
    path('get_csa_online_status/',views.get_csa_online_status,name='get_csa_online_status'),
    path('get_user_online_status/',views.get_user_online_status,name='get_user_online_status'),
path('update_user_current_message_count/',views.update_user_current_message_count,name="update_user_current_message_count"),
path('update_csa_current_message_count/',views.update_csa_current_message_count,name="update_csa_current_message_count"),

path('get_user_current_message_count/',views.get_user_current_message_count,name="get_user_current_message_count"),

path('get_csa_current_message_count/',views.get_csa_current_message_count,name="get_csa_current_message_count"),
path('get-videos/',views.get_videos,name="get-videos"),
    path('get-attachments/', views.get_attachments, name='get_attachments'),



  
  
  
  
  
  
   
  
]

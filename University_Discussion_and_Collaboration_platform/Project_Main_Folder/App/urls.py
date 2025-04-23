from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.view_notifications, name='view_notifications'),  # Notifications page
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/form/', views.form, name='form'),
    path('study/', views.study, name='study'),
    path('First/', views.First, name='First'),
    path('auth/', views.auth_view, name='auth'),
    path('jobs/', views.jobs, name='jobs'),
    path('chat-box/', views.chat_box, name='chat_box'),  # New URL pattern for the chat box
    path('reply_to_message/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('event_registration_page/', views.event_registration_page, name='event_registration_page'),
    
]
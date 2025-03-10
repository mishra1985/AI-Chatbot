# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # New default home view
    path('upload/', views.upload_document, name='upload_document'),
    path('chat/', views.chat_interface, name='chat'),
    path('ask/', views.ask_question, name='ask'),
]

from django.urls import path
from .views import AITutorView

urlpatterns = [
    path('chat/', AITutorView.as_view(), name='ai-chat'),
]

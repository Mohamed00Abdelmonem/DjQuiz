from django.urls import path
from .views import Question_List

urlpatterns = [
    path('q/', Question_List.as_view()),
]
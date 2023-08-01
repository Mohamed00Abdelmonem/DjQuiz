from django.urls import path
from .views import Question_List, Question_Detail

urlpatterns = [
    path('q/', Question_List.as_view()),
    path('q/<int:Q_id>/', Question_Detail),
]
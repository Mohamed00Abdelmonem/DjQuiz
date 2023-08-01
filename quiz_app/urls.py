from django.urls import path
from .views import Question_List, Question_Detail

urlpatterns = [
    path('', Question_List.as_view()),
    path('<int:Q_id>/', Question_Detail),
]
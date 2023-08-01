from django.urls import path
from .views import Question_List, Question_Detail, Question_Create, Question_Answer

urlpatterns = [
    path('', Question_List.as_view()),
    path('<int:Q_id>/', Question_Detail),
    path('create_q/', Question_Create.as_view()),
    path('create_a/', Question_Answer.as_view(),name='create_a'),
]
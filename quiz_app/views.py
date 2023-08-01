from django.shortcuts import render
from .models import Question, Answer
from django.views.generic import ListView, DetailView
# Create your views here.

class Question_List(ListView):
    model = Question
    context_object_name = "question"

def Question_Detail(request, Q_id):
    data = Question.objects.get(id=Q_id)
    answers = Answer.objects.filter(question_title=data)
    return render(request, 'quiz_app/qesiton_detail.html', {'Q':data, 'answers':answers})
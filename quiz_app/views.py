from django.shortcuts import render
from .models import Question, Answer
from django.views.generic import ListView, DetailView
# Create your views here.

class Question_List(ListView):
    model = Question
    context_object_name = "question"
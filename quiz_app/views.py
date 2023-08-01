from django.shortcuts import render, redirect

from .models import Question, Answer
from django.views.generic import ListView
# Create your views here.

class Question_List(ListView):
    model = Question
    context_object_name = "question"




def Question_Detail(request, Q_id):
    data = Question.objects.get(id=Q_id)
    answers = Answer.objects.filter(question_title=data)

    if request.method == 'POST':
        selected_answer_id = request.POST.get('answer')  # Get the ID of the selected answer from the form

        try:
            selected_answer = Answer.objects.get(id=selected_answer_id)
            if selected_answer.correct_answer:
                is_correct_answer = True
            else:
                is_correct_answer = False
        except Answer.DoesNotExist:
            is_correct_answer = False

    else:
        is_correct_answer = None

    return render(request, 'quiz_app/question_detail.html', {'Q': data, 'answers': answers, 'is_correct_answer': is_correct_answer})

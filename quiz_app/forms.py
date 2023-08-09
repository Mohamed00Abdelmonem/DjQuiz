# forms.py
from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['author','slug']  # Exclude the 'author' field from the form
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['author', 'question_title']  # Exclude the 'author' field from the form

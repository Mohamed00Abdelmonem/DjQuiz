from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from django.views.generic import ListView , CreateView, UpdateView, DeleteView
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



class Question_Create(CreateView):
    model = Question
    form_class = QuestionForm  # Use the custom form instead of specifying 'fields'

    def get_success_url(self):
        # Send a success message
        messages.success(self.request, 'Qeustion created successfully!')
        return reverse('indax')
        # success_url = '/'  # Replace with the desired URL

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    




# class Question_Answer(CreateView,):

#     model = Answer
#     form_class = AnswerForm

#     def get_success_url(self):
#         question_pk = self.kwargs['pk']
#         messages.success(self.request, 'Answer created successfully!')
#         return reverse('create_answer', kwargs={'pk': question_pk})
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         question_pk = self.kwargs['pk']
#         form.instance.question = Question.objects.get(pk=question_pk)

#         # Set the question title for the answer
#         question = Question.objects.get(pk=question_pk)
#         form.instance.question_title = question.title  # Use the 'title' attribute of the question

#         return super().form_valid(form)

    


def Question_Answer(request, A_id):
    question = Question.objects.get(id=A_id)  # Use get_object_or_404 to handle missing questions

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question_title = question
            answer.save()
            return redirect('/')  # Redirect to a success page or appropriate view
    
    else:
        form = AnswerForm()

    return render(request, 'quiz_app/answer_form.html', {'form': form})



# def Question_Answer(request, A_id):
#     data  = Question.objects.get(id = A_id)
#     answer = Answer.objects.get(question_title = data) 

#     if request.method == 'POST':
#         form = AnswerForm(request.POST, instance=data)
#         if form.is_valid():
#            form.save(commit = False)
#            form.author = request.user
#            form.question_title = answer
#            form.save()
#            return redirect('/')

#     else:
#         form = AnswerForm()
#     return render(request, 'quiz_app/answer_form.html', {'form':form})        









class Question_Update(UpdateView):
    model = Question
    fields = '__all__'
    success_url = '/'
    template_name = 'quiz_app/Quetion_update.html'



class Question_Delete(DeleteView):
    model = Question
    success_url = '/'



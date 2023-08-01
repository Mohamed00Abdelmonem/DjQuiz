from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.question_title
    
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    question_title = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"Answer {self.answer} for Q {self.question_title}"
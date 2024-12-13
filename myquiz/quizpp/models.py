'''from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # '1', '2', '3', or '4'

    def __str__(self):
        return self.text


class QuizSession(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    answered_correctly = models.IntegerField(default=0)
    answered_incorrectly = models.IntegerField(default=0)

    def __str__(self):
        return f"Session for {self.user}"
'''
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Question(models.Model):
    text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # '1', '2', '3', or '4'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.correct_option not in ('1', '2', '3', '4'):
            raise ValidationError('Correct option must be one of "1", "2", "3", or "4".')

    def __str__(self):
        return f"Question: {self.text[:50]}..."  # Truncate if long


class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    answered_correctly = models.IntegerField(default=0)
    answered_incorrectly = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session for {self.user.username} with score {self.score}"


class QuestionAttempt(models.Model):
    session = models.ForeignKey(QuizSession, on_delete=models.CASCADE, related_name='attempts')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attempt for {self.question.text[:50]}... - {'Correct' if self.is_correct else 'Incorrect'}"

    def clean(self):
        if self.selected_option not in ('1', '2', '3', '4'):
            raise ValidationError('Selected option must be one of "1", "2", "3", or "4".')

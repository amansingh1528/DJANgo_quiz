from django.urls import path
from .. import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.question, name='question'),
    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('result/', views.result, name='result'),
]

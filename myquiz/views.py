'''from django.shortcuts import render, redirect
from django.http import HttpResponse
from myquiz.quizpp.models import Question, QuizSession
import random

def start_quiz(request):
    if 'quiz_session_id' not in request.session:
        quiz_session = QuizSession.objects.create(user="User")
        request.session['quiz_session_id'] = quiz_session.id
    return redirect('question')

def get_random_question():
    questions = Question.objects.all()
    return random.choice(questions)

def question(request):
    quiz_session = QuizSession.objects.get(id=request.session['quiz_session_id'])
    if quiz_session.total_questions >= 10:  # End the quiz after 10 questions
        return redirect('result')

    question = get_random_question()
    return render(request, 'quiz/question.html', {'question': question})

def submit_answer(request, question_id):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        question = Question.objects.get(id=question_id)
        quiz_session = QuizSession.objects.get(id=request.session['quiz_session_id'])

        quiz_session.total_questions += 1
        if selected_option == question.correct_option:
            quiz_session.score += 1
            quiz_session.answered_correctly += 1
        else:
            quiz_session.answered_incorrectly += 1

        quiz_session.save()

        return redirect('question')

def result(request):
    quiz_session = QuizSession.objects.get(id=request.session['quiz_session_id'])
    return render(request, 'quiz/result.html', {'session': quiz_session})
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from myquiz.quizpp.models import Question, QuizSession
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import random

def start_quiz(request):

    if request.user.is_authenticated:
        if 'quiz_session_id' not in request.session:

            quiz_session = QuizSession.objects.create(user=request.user)
            request.session['quiz_session_id'] = quiz_session.id
        return redirect('question')
    else:

        return redirect('login')

def get_random_question():
    questions = Question.objects.all()
    return random.choice(questions)

def question(request):

    quiz_session = QuizSession.objects.get(id=request.session['quiz_session_id'])

    if quiz_session.total_questions >= 10:
        return redirect('result')

    question = get_random_question()
    return render(request, 'quiz/question.html', {'question': question})

def submit_answer(request, question_id):
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        question = Question.objects.get(id=question_id)
        quiz_session = QuizSession.objects.get(id=request.session['quiz_session_id'])

        quiz_session.total_questions += 1

        if selected_option == question.correct_option:
            quiz_session.score += 1
            quiz_session.answered_correctly += 1
        else:
            quiz_session.answered_incorrectly += 1

        quiz_session.save()

        return redirect('question')

def result(request):
    quiz_session = QuizSession.objects.get(id=request.session['quiz_session_id'])
    return render(request, 'quiz/result.html', {'session': quiz_session})
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('start_quiz')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
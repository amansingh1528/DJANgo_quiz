"""
URL configuration for myquiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.urls import path
from myquiz import views
urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('quiz/', include('myquiz.urls')),
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.question, name='question'),
    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('result/', views.result, name='result'),
]'''
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from myquiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Uncomment and use the following line if you want to include URLs from a separate 'myquiz' app
    # path('quiz/', include('myquiz.urls')),

    # URL pattern for the login view (built-in authentication login view)
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='templates/registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),

    # URL pattern for the logout view (built-in authentication logout view)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Your custom quiz views
    path('', views.start_quiz, name='start_quiz'),
    path('question/', views.question, name='question'),
    path('submit_answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('result/', views.result, name='result'),
]


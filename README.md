# Quiz Application

A simple Django-based quiz application where users can register, login, take a quiz, submit answers, and view results. The application uses Django's authentication system to manage users and sessions, and stores quiz data in the database.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **Quiz Sessions**: Users can take a quiz, track the number of questions answered, and view results.
- **Random Questions**: Randomized questions are fetched from the database for the quiz.
- **Scoring**: Correct and incorrect answers are counted, and users are provided with a score after the quiz.
- **Session Management**: The quiz session is tied to the logged-in user.

## Requirements

- Python 3.x
- Django 5.x
- SQLite (default database) or any other supported database

## Installation

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 2. Install the required packages

```bash
pip install django
django-admin starproject myquiz .
```

### 3. Apply migrations to set up the database

```bash
python manage.py migrate
```
### 4. Create a superuser to access the admin panel

```bash
python manage.py createsuperuser
```

### 5.Run the development server

```bash
python manage.py runserver
```

## File Structure
```bash
quiz-app/
├── myquiz/                   # Main app directory
│   ├── migrations/            # Database migrations
│   ├── templates/             # Template files (HTML)
│   │   └── registration/      # User authentication templates (login, signup)
│   │       └── login.html     # Login page template
│   │       └── signup.html    # Signup page template
│   ├── static/                # Static files (CSS, JS, Images)
│   ├── urls.py                # URL routing
│   ├── views.py               # Application logic and views
│   ├── models.py              # Data models
│   ├── admin.py               # Admin panel configuration
├── manage.py                  # Django management script
├── requirements.txt           # List of dependencies
└── db.sqlite3                 # SQLite database file (default)

```
### Running Tests
```bash
python manage.py test
```
## Author 
Aman Singh Chauhan



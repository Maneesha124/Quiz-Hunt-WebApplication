# Quiz Hunt - Django & PostgreSQL Quiz Management Platform

Quiz Hunt is a web application built with **Django** and **PostgreSQL** that allows users to participate in quizzes across different subjects. The application supports user management, subject categorization, question management, and quiz result evaluation. It is simple, scalable, and ideal for learning full-stack Django development.

## 🚀 Features

###  User Management
- Add new users  
- Delete users  
- User authentication (login/logout)

###  Subject Management
- Add new subjects  
- Organize quizzes by subjects  

###  Question Management
- Add question(s) to any subject  
- Edit or delete questions  
- Each question is mapped to a subject  

###  Quiz Features
- Attempt quizzes based on subjects  
- Score calculation and result page  
- View previous results (if implemented)

### Admin Panel
- Manage users, subjects, and questions  
- Django admin provides full CRUD operations  

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Backend | Django (Python) |
| Database | PostgreSQL |
| Frontend | HTML, CSS, Bootstrap |
| Server | Django Development Server |

## 📂 Project Structure

QUIZSITE/
│
├── quiz/ # Main application
│ ├── templates/ # HTML pages
│ ├── migrations/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Database models
│ ├── views.py # View functions
│ ├── urls.py # App URL routes
│ └── tests.py
│
├── quizsite/ # Django project config
│ ├── settings.py
│ ├── urls.py # Global URLs
│ ├── asgi.py
│ └── wsgi.py
│
├── db.sqlite3 (if using SQLite locally)
├── manage.py
└── README.md
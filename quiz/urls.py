from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz'),
    path('quiz/<int:quiz_id>/result/', views.result, name='result'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

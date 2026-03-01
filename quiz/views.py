from django.shortcuts import render
from .models import Quiz, Question

def home(request):
    quizzes = Quiz.objects.all()
    return render(request, 'home.html', {'quizzes': quizzes})

def quiz_view(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, 'quiz.html', {'quiz': quiz, 'questions': questions})

def result(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    score = 0
    for q in questions:
        selected = request.POST.get(str(q.id))
        if selected and int(selected) == q.correct_option:
            score += 1
    return render(request, 'result.html', {'score': score, 'total': questions.count()})

def dashboard(request):
    context = {
        'quiz_count': Quiz.objects.count(),
        'question_count': Question.objects.count(),
    }
    return render(request, 'dashboard.html', context)

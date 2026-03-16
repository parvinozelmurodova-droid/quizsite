from django.shortcuts import render

from .models import Question

def quiz_view(request):

    questions = Question.objects.all()

    if request.method == "POST":
        
        user_answer = request.POST.get("answer")
        question_id = request.POST.get("question_id")

        question = Question.objects.get(id=question_id)

        correct = user_answer == question.correct_answer

        return render(request,"result.html",{
            "question":question,
            "user_answer":user_answer,
            "correct":correct
        })
        
        
    return render(request,"quiz.html",{"questions":questions})

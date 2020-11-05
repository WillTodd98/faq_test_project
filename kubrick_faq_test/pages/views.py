from django.shortcuts import render
from django.http import HttpResponse
from faq_log.models import Question

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def questions_view(request, *args, **kwargs):
    my_context = {
        "my_list": [123, 1234, 12345]
    }
    return render(request, "questions.html", my_context)

def question_list_view(request):
    queryset = Question.objects.all()
    context = {
        "object_list": queryset 
    }
    return render(request, "questions_list.html", context)
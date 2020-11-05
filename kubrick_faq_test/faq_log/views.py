from django.shortcuts import render, get_object_or_404, redirect

from django.http import Http404
from faq_log.models import Question
from .forms import QuestionForm

def question_create_view(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
          form.save()
    
    context = {
        'form': form
    }
    return render(request, "question_create.html", context)

# def question_create_view(request):
    # context = {}
    # return render(request, "question_create.html", context)

def question_lookup_view(request, my_id):
    obj = get_object_or_404(Question, id=my_id)   
    context = {
        'object': obj
    }
    return render(request, "question_detail.html", context)

def question_delete_view(request, my_id):
    obj = get_object_or_404(Question, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect("../../")
    context = {
        "object": obj
    }
    return render(request, "question_delete.html", context)

def question_list_view(request):
    queryset = Question.objects.all()
    context = {
        "object_list": queryset 
    }
    return render(request, "questions_list.html", context)
from django.shortcuts import render
# from django import views

# Create your views here.
from django.http import HttpResponse
from myapp.models   import Question
from myapp.models   import Choice


def index(request):
    return HttpResponse("Welcome")


def ques(request):
    questions = Question.objects.all()
    return render(request,"ques.html",{'questions':questions})


def option(request,id):
    context={}
    context["django"]=Choice.objects.filter(question=id)
    
    return render(request,"index.html",context)

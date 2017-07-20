from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World.  your're at the polls index work")

def results(request, question_id):
    response = "You're looking at the result of question %s."
    return HttpResponse(response % question_id)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting o question %s." %question_id)



from django.shortcuts import render

# Imported the class HttpResponse from the django and http modules
from django.http import HttpResponse

#This is a function that is indexing the variable onto the poll website so when i follow
##the link this str will appear on the webpage
def index(request):
    return HttpResponse("Hello, world. Welcome to Eli's polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
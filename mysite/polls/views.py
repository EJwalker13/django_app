from django.http import Http404
from django.shortcuts import render

# Imported the class HttpResponse from the django and http modules
from django.http import HttpResponse

from .models import Question

#This is a function that is indexing the variable onto the poll website so when i follow
##the link this str will appear on the webpage
def index(request):
    return HttpResponse("Hello, world. Welcome to Eli's polls index.")

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #this orders the fields in the 'Question' model by the publication date 
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

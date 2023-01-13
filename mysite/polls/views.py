from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from requests import request

from mysite.polls.tests import QuestionModelTests

from .models import Choice, Question 

#This is a function that is indexing the variable onto the poll website so when i follow
##the link this str will appear on the webpage
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order.by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class vote(request, question_id):
    model = Question
    template_name = "polls/results.html"



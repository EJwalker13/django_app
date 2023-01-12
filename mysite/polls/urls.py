#This file creates a URL configuration
from django.urls import path
from . import views #Imported and accessed the polls.views file

#In views I created this index function so now this function takes my index function
##and prints my written string variable on the polls website by following the path.
app_names = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # this path connects the detail function in views.py 
    path('<int:question_id>/results/', views.results, name='results'), # this path connects the results function in views.py 
    path('<int:question_id>/vote/', views.vote, name='vote'), # this path connects the vote function in views.py 
]

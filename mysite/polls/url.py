#This file creates a URL configuration
from django.urls import path
from . import views #Imported and accessed the polls.views file

#In views I created this index function so now this function takes my index function
##and prints my written string variable on the polls website by following the path.
urlpatterns = [
    path('', views.index, name='index'),
    # this links the poll's identification number to the 
    path('<int:question_id>/', views.detail, name='detail'), 

]

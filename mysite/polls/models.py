from django.db import models #accessed the models module from djangos database module

import datetime
from django.db import models
from django.utils import timezone


#Created a class called questions ("Model" is a class)
class Question(models.Model):
    question_text = models.CharField(max_length=200) #this field instance defines the character length (or data) for the questions' text within the class
    pub_date = models.DateTimeField('date time') #this field instance adds a field for the date the question was published
    def __str__(self):
        return self.question_text  #this function returns the str found in the object question_text
    def was_published_recently(self): #this function returns the 
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) #function returns the publication date and time of the question was created

#Created a second class for choices
class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE) #this field instance lets Django know many choices are related to one question
    choice_text = models.CharField(max_length=200) #this field instance defines the character length for the choices' text within the class
    votes = models.IntegerField(default=0) #this field instance going to store the number of votes in the poll
    def __str__(self):
        return self.choice_text




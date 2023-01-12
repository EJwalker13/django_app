"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path #This connects my polls URL.py to the main URL webage http://127.0.0.1:8000/

urlpatterns = [
    path('polls/', include('polls.url')),#this function is calling my written function configured via the urls in polls.url/polls.views.py to be plug into the admin site
    path('admin/', admin.site.urls), #this new variable connects the function previously written above then connects this with the index function from polls.url/polls.views.py 
]

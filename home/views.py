from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.
def example_fun(request):
    tasks = Task.objects.all()
    response = ", ".join([task.title for task in tasks])
    return HttpResponse(response)

#create a  model for storing information about places
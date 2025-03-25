from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskList
# Create your views here.
def index(request):
        return HttpResponse("No Tasks in To-do Lists")


def create_task(request):
        pass
            

def view_task(request):
    tasks = TaskList.object.all()
    return (request, {'Available tasks': {tasks}})

def get_task():
       pass
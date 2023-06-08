from django.shortcuts import render, HttpResponse
from todoapp.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks' : tasks,
        'complete' : completed_task,
    }
    return render(request, 'home.html', context)



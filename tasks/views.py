from django.shortcuts import render, redirect
from tasks.models import Task
from .forms import *
# Create your views here.


def index(request):

    # For adding a new task
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    # For rendering the tasks on the page
    all_tasks = Task.objects.all()
    params = {'all_tasks': all_tasks, 'form': form}
    return render(request, 'index.html', params)


def update_task(request, myid):
    task = Task.objects.get(id=myid)
    # if you just pass TaskForm it will give a blank form
    form = TaskForm(instance=task)
    # Because instance = task is given, it will be pre-filled with that task

    params = {'form': form}
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)#Here instance is required again because
                                                      #if we dont do so, it will create a new item instead of updatig it
                                                      #We are saying that we are giving in new data but still updating
                                                      #the insatnce of the old item
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'update_task.html', params)

def delete_task(request, myid):
    task = Task.objects.get(id = myid)
    params = {'task':task} #Required for rendering the data

    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete_task.html', params)

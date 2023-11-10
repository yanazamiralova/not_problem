from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта',
                                               'tasks': tasks})

def create(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/task-delete.html'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = '/'
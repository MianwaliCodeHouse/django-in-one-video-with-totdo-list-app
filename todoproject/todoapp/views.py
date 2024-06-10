from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.template import loader

def index(request):
    todos = Todo.objects.all().order_by('-id')
    template = loader.get_template('index.html')
    context={
        'todos':todos,
    }
    return HttpResponse(template.render(context,request))

def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    template = loader.get_template('add_todo.html')
    context={
        'form':form,
    }
    return HttpResponse(template.render(context,request))

def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    template = loader.get_template('edit_todo.html')
    context={
        'form':form,
    }
    return HttpResponse(template.render(context,request))

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('index')
    template = loader.get_template('delete_todo.html')
    context={
        'todo':todo,
    }
    return HttpResponse(template.render(context,request))
    # return render(request, 'todoapp/delete_todo.html', {'todo': todo})
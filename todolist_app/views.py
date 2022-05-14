from email import message
from django.shortcuts import redirect, render
from todolist_app.models import DoList
from todolist_app.form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

context = {
    "welcome": "Hello, Motherfuckers!!!!",
}


@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
        messages.success(request,"All ok")
        return redirect("todolist")
    else:
        all_task = DoList.objects.filter(owner=request.user)
        paginator = Paginator(all_task, 10)
        page = request.GET.get('page')
        all_task = paginator.get_page(page)   
        return render(request, 'todo.html', {"all_tasks": all_task})

@login_required
def delete_task(request, task_id):
    task = DoList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.success(request,("You have no power here!"))
    return redirect("todolist")

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = DoList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        
        messages.success(request,("Edit complete"))
        return redirect("todolist")
    else:
        task_obj = DoList.objects.get(pk=task_id)
        return render(request, 'edit.html', {"task_obj": task_obj})

@login_required
def complete_task(request, task_id):
    task = DoList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.do = True
        task.save()
    else:
        messages.success(request,("You have no power here!"))
    return redirect("todolist")

@login_required
def pending_task(request, task_id):
    task = DoList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.do = False
        task.save()
    else:
        messages.success(request,("You have no power here!"))
    return redirect("todolist")

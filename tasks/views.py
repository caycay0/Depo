from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Task
from .forms import TaskForm, UserRegisterForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user, completed=False)
    do_tasks = tasks.filter(category='urgent_important')
    decide_tasks = tasks.filter(category='not_urgent_important')
    delegate_tasks = tasks.filter(category='urgent_not_important')
    delete_tasks = tasks.filter(category='not_urgent_not_important')

    context = {
        'do_tasks': do_tasks,
        'decide_tasks': decide_tasks,
        'delegate_tasks': delegate_tasks,
        'delete_tasks': delete_tasks,
    }
    return render(request, 'tasks/task_list.html', context)

@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'tasks/completed_tasks.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Görevi oturum açmış kullanıcıya atama
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Yalnızca oturum açmış kullanıcıya ait görevleri alır
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Yalnızca oturum açmış kullanıcıya ait görevleri alır
    task.delete()
    return redirect('task_list')

@login_required
def task_toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)  # Yalnızca oturum açmış kullanıcıya ait görevleri alır
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def home(request):
    return render(request, 'tasks/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('task_list')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todo_data = Task.objects.filter(user=request.user)
    var = request.COOKIES.get('last_login', 'UserNotFound')
    if var == "UserNotFound":
        return HttpResponseRedirect(reverse("todolist:login"))
    context = {
        'list_todo': todo_data,
        'username' : request.user.username,
        'last_login': var,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('todo')
        description = request.POST.get('desc')
        date = datetime.datetime.now()
        Task.objects.create(user=user, title=title, description=description, date=date)
        return HttpResponseRedirect(reverse('todolist:show_todolist'))
    return render(request, 'taskform.html')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    data = Task.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def change_status(request, id):
    data = Task.objects.get(id=id)
    if data.is_finished == False:
        data.is_finished = True
    else:
        data.is_finished = False
    data.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))


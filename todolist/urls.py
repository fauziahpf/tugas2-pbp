from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
    path('change/<int:id>/', change_status, name='change_status'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('json/', show_json, name="show_json"),
    path('add/', todolist_ajax, name="todolist_ajax" )
]
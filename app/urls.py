from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addtodo',views.addtodo,name='addtodo'),
    path('delete/<int:todo_id>',views.delete,name='delete'),
]
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import todo
# Create your views here.
def home(request):
    todos = todo.objects.all().order_by("added_date")
    tds = {'todos': todos}
    return render(request,'app/index.html',tds)


def addtodo(request):

    added_date=timezone.now()
    content=request.POST['content']
    if content:
        todo.objects.create(added_date=added_date,text=content)
        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')
    #return HttpResponseRedirect('/')

def delete(request,todo_id):
    ob=todo.objects.filter(id=todo_id)
    ob.delete()

    return HttpResponseRedirect('/')
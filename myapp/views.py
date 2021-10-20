from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from myapp.forms import TodoForm

from myapp.models import Todo

# Create your views here.

def addTodo(request):
    todoform = TodoForm(request.POST or None)
    if todoform.is_valid():
        todoform.save()
        return redirect('/')
    return render(request, 'addTodo.html', {'form': todoform})
    


def Index_page(request):
    data=Todo.objects.all()
    return render(request,'index.html',{'data':data})
    
def update(request,id):
    pickTodo = Todo.objects.get(pk=id)
    editForm = TodoForm(request.POST or None, instance=pickTodo)

    if editForm.is_valid():
        editForm.save()
        return redirect('/')

    return render(request, 'edit.html', {'form': editForm})

    




def delete(request,id):
    deleteTodo=Todo.objects.get(id=id)
    deleteTodo.delete()
    return redirect('/')


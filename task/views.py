from django.shortcuts import render,redirect
from .forms import Task,Category
from .models import TaskModel,TaskCategory
# Create your views here.

def addtask(request):
    if request.method=='POST':
        form=Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Task()
    heading="Add Task"
    return render(request,'form.html',{'form':form,'heading':heading})            

def addcategory(request):
    if request.method=='POST':
        print(request.POST)
        form=Category(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Category()
        print(form.errors)
    heading="Add Category"
    return render(request,'form.html',{'form':form,'heading':heading})
                
def showtask(request):
    task=TaskModel.objects.all()
    return render(request,'showtask.html',{'task':task})
    
def edittask(request,id):
    task=TaskModel.objects.get(id=id)
    if request.method=='POST':
        form=Task(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('showtask')
    else:
        form=Task(instance=task)
        heading="Edit Task"
    return render(request,'form.html',{'form':form,'heading':heading})           

def deletetask(request,id):
    task=TaskModel.objects.get(id=id)
    task.delete()
    return redirect('showtask')
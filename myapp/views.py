from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *

# Create your views here.
def display(request):
    s=Employee.objects.all()
    d={'emp':s}
    return render(request,"index.html",d)

def insert_view(request):
    f=EmployeeForms()
    if request.method=='POST':
        f=EmployeeForms(request.POST)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'forms':f}
    return render(request,'insert_update.html',d)

def delete_view(request,id):
    if request.method == 'POST':
        s=Employee.objects.get(id=id)
        s.delete()
        return redirect('/')
    return render(request, 'index.html', {'delete': True})

def update_view(request,id):
    s=Employee.objects.get(id=id)
    f=EmployeeForms(instance=s)
    if request.method=='POST':
        f=EmployeeForms(request.POST, instance=s)
        if f.is_valid():
            f.save(commit=True)
        return redirect('/')
    d={'forms': f, 'emp':s}
    return render(request,'insert_update.html',d)
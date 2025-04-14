from django.shortcuts import render,redirect
from myapp.models import *
from myapp.forms import *
#api-imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.serializers import EmployeeSerializer


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

# api---views
@api_view(['GET'])
def api_display(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_insert(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({'message': 'Employee deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def api_update(request, id):
    try:
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
    
from django.shortcuts import render,redirect
from.models import*

# Create your views here.

def homepage(request):
    return render(request,'home.html')  #loads home.html when homepage is run

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

#model class
def student(request):
    student=student.object.all()
    return render(request,'student.html')

def employee(request):
    employee=employee.object.all()
    return render(request,'employee.html')

def car(request):
    car=car.object.all()
    return render(request,'car.html')

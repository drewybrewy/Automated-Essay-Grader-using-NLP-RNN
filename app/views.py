import sys

sys.path.append('C:/Users/LENOVO/Desktop/aeg/proj/grader')
import processing
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import Students
from .models import Essays
from django.contrib import messages
import time


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index1(request):
    return render(request, 'index1.html')

@csrf_exempt
def func2(request):

    first_name = request.POST['first_name']
    last_name = request.POST['lname']
    roll_no = int(request.POST['roll_no'])
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    request.session['email'] = email

    student = Students()
    student.first_name = first_name
    student.last_name = last_name
    student.roll_no = roll_no
    student.email = email
    student.password = password
    student.gender = gender
    student.save()

    return render(request, 'func2.html', { 'first_name':first_name, 'last_name': last_name, 'roll_no':roll_no, 'email':email, 'password':password, 'gender':gender})

@csrf_exempt
def func(request):

    email1 = request.POST['email']
    password1 = request.POST['password']
    request.session['email'] = email1

    if  not Students.objects.filter(email = email1, password = password1).exists():
        #raise ValidationError("Incorrect Username or Password")
        #print("Incorrect Username or Password")
        messages.info(request, "Incorrect Username or Password")
        time.sleep(1)
        #return render(request,'index1.html')
        return redirect('index1')

    else:
        return render(request, 'func2.html')

@csrf_exempt
def grade(request):

    title = request.POST['title']
    essay = request.POST['essay']
    email = request.session['email']
    grade = processing.prediction(essay)
    student = Students.objects.get(email=email)
    essay1 = Essays(title = title, essay = essay, grade = grade, students = student)
    essay1.save()
    title = Essays.objects.all().values('title','grade')

    return render(request, 'grades.html',{'title':title})

def grades(request):

    title = Essays.objects.all().values('title','grade')

    return render (request, 'grades.html',{'title':title})

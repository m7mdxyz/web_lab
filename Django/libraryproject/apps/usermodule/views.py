from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import models, Student, Student2, ImageModel
from .forms import StudentForm, Student2Form, ImageForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Public Views (No login required)
def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):  # Add the view function (index2)
    return HttpResponse("value1 = " + str(val1))

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'You have successfully registered!')
                return redirect('login')  # Redirect to login page
            except:
                messages.error(request, 'Error: Username already exists!')
        else:
            messages.error(request, 'Passwords do not match!')

    return render(request, 'usermodule/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('list_students')  # Redirect to list_students
        else:
            messages.error(request, 'Invalid username or password!')

    return render(request, 'usermodule/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


# Protected Views (Login required)
@login_required(login_url='login')
def lab8_task7(request):
    student_counts = Student.objects.values('address__city').annotate(count=models.Count('id'))
    return render(request, 'usermodule/lab8_task7.html', {'student_counts': student_counts})


# Lab 10 Task 1: CRUD for Student
@login_required(login_url='login')
def list_students(request):
    students = Student.objects.all()
    return render(request, 'usermodule/list_students.html', {'students': students})

@login_required(login_url='login')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_student.html', {'form': form})

@login_required(login_url='login')
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/update_student.html', {'form': form})

@login_required(login_url='login')
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('list_students')


# Lab 10 Task 2: CRUD for Student2
@login_required(login_url='login')
def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/list_students2.html', {'students': students})

@login_required(login_url='login')
def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'usermodule/add_student2.html', {'form': form})

@login_required(login_url='login')
def update_student2(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'usermodule/update_student2.html', {'form': form})

@login_required(login_url='login')
def delete_student2(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    student.delete()
    return redirect('list_students2')


# Lab 10 Task 3: CRUD for ImageModel
@login_required(login_url='login')
def list_images(request):
    images = ImageModel.objects.all()
    return render(request, 'usermodule/list_images.html', {'images': images})

@login_required(login_url='login')
def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageForm()
    return render(request, 'usermodule/upload_image.html', {'form': form})

@login_required(login_url='login')
def delete_image(request, image_id):
    image = get_object_or_404(ImageModel, id=image_id)
    image.delete()
    return redirect('list_images')

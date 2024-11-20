from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import models, Student, Student2, ImageModel
from .forms import StudentForm, Student2Form, ImageForm


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

def lab8_task7(request):
    student_counts = Student.objects.values('address__city').annotate(count=models.Count('id'))
    return render(request, 'usermodule/lab8_task7.html', {'student_counts': student_counts})

# lab 10 task 1 views
def list_students(request):
    students = Student.objects.all()
    return render(request, 'usermodule/list_students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/add_student.html', {'form': form})

def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/update_student.html', {'form': form})

def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('list_students')

# lab 10 task 2 views
def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'usermodule/list_students2.html', {'students': students})

def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'usermodule/add_student2.html', {'form': form})

def update_student2(request, student_id):
    student = Student2.objects.get(id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'usermodule/update_student2.html', {'form': form})

def delete_student2(request, student_id):
    student = Student2.objects.get(id=student_id)
    student.delete()
    return redirect('list_students2')

#lab 10 task 3
def list_images(request):
    images = ImageModel.objects.all()
    return render(request, 'usermodule/list_images.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageForm()
    return render(request, 'usermodule/upload_image.html', {'form': form})

def delete_image(request, image_id):
    image = ImageModel.objects.get(id=image_id)
    image.delete()
    return redirect('list_images')
from django.shortcuts import render
from django.http import HttpResponse
from .models import models, Student


def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

def lab8_task7(request):
    student_counts = Student.objects.values('address__city').annotate(count=models.Count('id'))
    return render(request, 'usermodule/lab8_task7.html', {'student_counts': student_counts})

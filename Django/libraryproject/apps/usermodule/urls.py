from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('lab8/task7', views.lab8_task7, name="users.lab8_task7"),
    # lab 10 task 1 URLs
    path('students/', views.list_students, name='list_students'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/update/<int:student_id>/', views.update_student, name='update_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    # lab 10 task 2 URLs
    path('students2/', views.list_students2, name='list_students2'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('students2/update/<int:student_id>/', views.update_student2, name='update_student2'),
    path('students2/delete/<int:student_id>/', views.delete_student2, name='delete_student2'),
    # lab 10 task 3 URLs
    path('images/', views.list_images, name='list_images'),
    path('images/upload/', views.upload_image, name='upload_image'),
    path('images/delete/<int:image_id>/', views.delete_image, name='delete_image'),
]
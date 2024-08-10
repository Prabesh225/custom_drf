"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moix import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.Student_detail.as_view(), name='students'),  # API endpoint for getting all students
    # path('students/create/', views.student_create.as_view(), name='student_create'),  # API endpoint for creating a new student
    path('students/retrive/<int:pk>/', views.student_retrive.as_view(), name='student_edit'), # API endpoint for editing a student
    # path('students/update/<int:pk>/', views.student_update.as_view(), name='student_update'),  # API endpoint for updating a student
    # path('students/delete/<int:pk>/', views.student_delete.as_view(), name='student_delete'),  # API endpoint for deleting a student
]

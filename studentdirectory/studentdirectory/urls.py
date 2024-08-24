"""
URL configuration for studentdirectory project.

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

from django.urls import path
from my_app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('students/', views.student_index, name='student-index'),
    path('students/<int:student_id>/', views.student_detail, name='student-detail'),
    path('students/create/', views.StudentCreate.as_view(), name='student-create'),
    path('students/<int:pk>/update/', views.StudentUpdate.as_view(), name='student-update'),
    path('students/<int:pk>/delete', views.StudentDelete.as_view(), name='student-delete'),
    path(
        'students/<int:student_id>/add-studentjob/', 
        views.add_studentjob, 
        name='add-studentjob'
    ),
    path('availablejobs/create/', views.AvailableJobsCreate.as_view(), name='availablejobs-create'),
    path('availablejobs/<int:pk>/', views.AvailableJobsDetail.as_view(), name='availablejobs-detail'),
    path('availablejobs/', views.AvailableJobsList.as_view(), name='availablejobs-index'),
        #Existing urls above
    path('availablejobs/<int:pk>/update/', views.AvailableJobsUpdate.as_view(), name='availablejobs-update'),
    path('availablejobs/<int:pk>/delete/', views.AvailableJobsDelete.as_view(), name='availablejobs-delete'),
    # New URL to associate a toy with a cat
    path('students/<int:student_id>/associate-availablejobs/<int:availablejobs_id>/', views.associate_availablejobs, name='associate-availablejobs'),
    path('students/<int:student_id>/remove-availablejobs/<int:availablejobs_id>/', views.remove_availablejobs, name='remove-availablejobs'),


    

]

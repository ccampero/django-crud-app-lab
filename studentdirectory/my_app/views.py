from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student, AvailableJobs
from .forms import StudentJobsForm
from django.contrib.auth.views import LoginView

# Create your views here.

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def student_index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students })

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    studentjobs_form = StudentJobsForm()
    return render(request, 'students/detail.html', {
        'student': student, 'studentjobs_form': studentjobs_form,
        'availablejobs': availablejobs_student_doesnt_have
        })

def add_studentjob(request, student_id):
    form = StudentJobsForm(request.POST)
    if form.is_valid():
        new_studentjob = form.save(commit=False)
        new_studentjob.student_id = student_id
        new_studentjob.save()
    return redirect('student-detail', student_id=student_id)

def associate_availablejobs(request, student_id, availablejobs_id):
    Student.objects.get(id=student_id).availablejobs.add(availablejobs_id)
    return redirect('student-detail', student_id=student_id)

def remove_availablejobs(request, student_id, availablejobs_id):
   student = Student.objects.get(id=student_id),
   availablejobs = availablejobs.objects.get(id=availablejobs_id)
   student.availablejobs.remove(availablejobs)
   
   return redirect('student-detail', student_id=student.id)

class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'age', 'birthday', 'about']
    success_url = '/students/'

class StudentUpdate(UpdateView):
    model = Student
    fields = ['age', 'birthday', 'about']
    
class StudentDelete(DeleteView):
    model = Student
    success_url = '/students/'

class AvailableJobsCreate(CreateView):
    model = AvailableJobs
    fields = '__all__'

class AvailableJobsList(ListView):
    model = AvailableJobs
    
class AvailableJobsDetail(DetailView):
    model = AvailableJobs
    
class AvailableJobsUpdate(UpdateView):
    model = AvailableJobs
    fields = ['name', 'color']
    
class AvailableJobsDelete(DeleteView):
    model = AvailableJobs
    success_url = '/availablejobs/'
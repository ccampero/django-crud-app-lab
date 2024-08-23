from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student
from .forms import StudentJobsForm

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
        'student': student, 'studentjobs_form': studentjobs_form
        })

# def add_studentjob(request, student_id):
#     form = StudentJobsForm(request.POST)
    # if form.is_valid():
    #     new_studentjob = form.save(commit=False)
    #     new_studentjob.student_id = student_id
    #     new_studentjob.save()
    # return redirect('student-detail', student_id=student_id)
# views.py

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
    

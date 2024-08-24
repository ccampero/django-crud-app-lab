from django.contrib import admin
from .models import Student, StudentJobs, AvailableJobs

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentJobs)
admin.site.register(AvailableJobs)

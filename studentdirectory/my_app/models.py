from datetime import date, datetime
from django.db import models
from django.urls import reverse

JobStatus = (
    ('Y', 'Yes job done'),
    ('N', 'No job not done')
)


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(default=date.today)
    about = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'student_id': self.id})
    

class StudentJobs(models.Model):
    date = models.DateField(default=date.today)
    job = models.CharField(
        max_length=1,
        choices=JobStatus,
        default=JobStatus[0][0]
        )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_job_display()} on {self.date}"
    class Meta:
        ordering = ['-date']
    
    
    
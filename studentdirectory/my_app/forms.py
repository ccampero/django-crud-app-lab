from django import forms
from .models import StudentJobs

class StudentJobsForm(forms.ModelForm):
    class Meta:
        model = StudentJobs
        fields = ['date', 'job']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

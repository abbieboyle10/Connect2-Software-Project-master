from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from account.models import *


class EmployerModelForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('company_name', 'phone', 'email',
                  'sector', 'avatar', 'county', 'city')


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'location', 'description_role',
                  'contract', 'office_type', 'length', 'num_hires', 'description_personality', 'enviornment',)

        labels = {
            "title": "Job title",
            "location": "Location",
            "description_role": "Description of the role",
            "office_type": "Can this job be performed remotely, meaning primarily from home? If so, we’ll add a 'Remote' tag to your post",
            "length": "Type of contract",
            "num_hires": "How many people are you hiring?",
            "description_personality": "Please describe the ideal canidates personality",
            "enviornment": "Please describe the work enviornment, the future employees role within the team and interaction with co-workers"

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City or Town'}),
            'description_role': forms.TextInput(attrs={'class': 'form-control'}),
            'contract': forms.Select(attrs={'class': 'form-control'}),
            'office_type': forms.Select(attrs={'class': 'form-control'}),
            'length': forms.Select(attrs={'class': 'form-control'}),
            'num_hires': forms.TextInput(attrs={'class': 'form-control'}),
            'description_personality': forms.TextInput(attrs={'class': 'form-control'}),
            'enviornment': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InterviewForm(ModelForm):
    class Meta:
        model = InterviewPlan
        date = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
        fields = ('date',  'location',
                  'platform',)
        labels = {
            "date": "Date of interview",
            "location": "Location",
            "platform": "Platform",

        }

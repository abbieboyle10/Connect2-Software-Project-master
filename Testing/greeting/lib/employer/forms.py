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
        fields = ('title', 'city', 'description_role',
                  'contract', 'office_type', 'length',  'description_personality', 'enviornment')

        labels = {

            "City": "City",
            "description_role": "Role Responsibilities",
            "office_type": "Can this job be performed remotely, meaning primarily from home? If so, we’ll add a 'Remote' tag to your post",
            "length": "Type of contract",

            "description_personality": "Role Description",
            "enviornment": "Daily Role"

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of Role'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City or Town'}),
            'description_role': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please describe the daily and long term responsibilities'}),
            'contract': forms.Select(attrs={'class': 'form-control'}),
            'office_type': forms.Select(attrs={'class': 'form-control'}),
            'length': forms.Select(attrs={'class': 'form-control'}),

            'description_personality': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please list a minimum of ten words describing the candidates role within their team. Will they be required to take a leadership role? Will they be required to support and teach others? '}),
            'enviornment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please describe the daily or reoccuring tasks involved within the role '}),
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


class JobSkillForm(ModelForm):
    class Meta:
        model = JobSkill
        fields = ('title',  'level',
                  'years_of',)

        labels = {

            "title": "Title of Skill",
            "level": "Expected Level",
            "years_of": "Years of Experience",


        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'years_of': forms.Select(attrs={'class': 'form-control'}),

        }


class JobTagForm(ModelForm):
    class Meta:
        model = JobTag
        fields = ('title',  'category')

        labels = {

            "title": "Title of Skill",
            "category": "Category",



        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),


        }

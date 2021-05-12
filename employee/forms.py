from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from account.models import *


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'tag', 'sector', 'avatar', 'county', 'city')


class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('cover_letter',)

        labels = {
            "cover_letter": "Include optional cover letter here",
        }
        widgets = {
            'cover_letter': forms.Textarea(attrs={'class': 'form-control'}),

        }


class SkillForm(ModelForm):
    class Meta:
        model = EmployeeSkill
        fields = ('title',  'level', 'years_of')
    labels = {

        "title": "Title of Skill",
        "level": "Level",
        "years_of": "Years of Experience",



    }
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'level': forms.Select(attrs={'class': 'form-control'}),
        'years_of': forms.Select(attrs={'class': 'form-control'}),


    }


class TagForm(ModelForm):
    class Meta:
        model = PersonTag
        fields = ('title',  'category')


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

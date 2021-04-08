from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from account.decorators import employee_required, employee_check
from account.models import Employee, EmployeeSkill, Job, MatchedSkills
from .forms import SkillForm, ExperienceForm
from django.contrib.auth.decorators import user_passes_test
from personality.models import Quiz, Result, Personality
from .forms import EmployeeModelForm, ApplyJobForm


@user_passes_test(employee_check, login_url='employer-home')
def employee_home(request):
    user = request.user

    context = {
        'user': user,



    }
    return render(request, 'employee/employee-home.html', context)
    # return HttpResponse('Hello world')


@login_required(login_url='login')
@user_passes_test(employee_check, login_url='employer-profile')
def employee_profile(request, pk=None):

    employee = Employee.objects.get(user=request.user)
    form = EmployeeModelForm(request.POST or None,
                             request.FILES or None, instance=employee)
    skills = employee.employeeskill_set.all()
    results = employee.result_set.all()
    personalitys = Personality.objects.filter(employee=employee)
    experiences = employee.experience_set.all()
    quizs = Quiz.objects.all()
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'employee': employee,
        'skills': skills,
        'experiences': experiences,
        'quizs': quizs,
        'results': results,
        'personalitys': personalitys,
        'form': form,
        'confirm': confirm,


    }

    return render(request, 'employee/profile.html', context)


@user_passes_test(employee_check, login_url='jobs')
def personality_page(request):

    return render(request, 'employee/personality.html')


@user_passes_test(employee_check, login_url='jobs')
def find_job(request):
    jobs = Job.objects.all()

    context = {'jobs': jobs}
    return render(request, 'employee/findjob.html', context)


def createSkill(request):
    form = SkillForm()
    employee = Employee.objects.get(user=request.user)
    skills = employee.employeeskill_set.all()
    experiences = employee.experience_set.all()
    context = {'employee': employee, 'skills': skills,
               'experiences': experiences, }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'employee/profile.html', context)

    context = {'form': form}
    return render(request, 'employee/skills_form.html', context)


def createExperience(request):
    form = ExperienceForm()
    employee = Employee.objects.get(user=request.user)
    experiences = employee.experience_set.all()
    skills = employee.employeeskill_set.all()
    context = {'employee': employee,
               'experiences': experiences, 'skills': skills, }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'employee/profile.html', context)

    context = {'form': form}
    return render(request, 'employee/experiences_form.html', context)


def viewjob(request, pk):
    employee = Employee.objects.get(user=request.user)
    form = EmployeeModelForm(request.POST or None,
                             request.FILES or None, instance=employee)
    form2 = ApplyJobForm()
    jobs = Job.objects.filter(pk=pk)
    candidate = Employee.objects.get(user=request.user)
    job = Job.objects.get(pk=pk)
    employeeskills = employee.employeeskill_set.all().values_list('title',
                                                                  flat=True).distinct()
    print(employeeskills)
    jobskills = job.jobskill_set.all().values_list('title', flat=True).distinct()
    print(jobskills)
    employeeskills_as_set = set(employeeskills)
    intersection = employeeskills_as_set.intersection(jobskills)
    intersection_as_list = list(intersection)
    print(intersection_as_list)
    matched_amount = len(intersection_as_list)
    print(matched_amount)

    personality = Personality.objects.get(employee=employee)
    person_type = personality.group
    job_type = job.ideal_person

    if request.method == 'POST':
        form2 = ApplyJobForm(request.POST)

        if form2.is_valid():
            application = form2.save(commit=False)
            application.job = job
            application.candidate = candidate
            application.status = 'applied'
            application.person_type = person_type
            application.job_type = job_type
            application.save()
            score = 0
            print(job_type)
            print(person_type)
            if job_type == person_type:

                application.match = True
                score += 1

            else:

                application.match = False

            for x in intersection_as_list:
                MatchedSkills.objects.create(application=application, title=x)

                score += 1
                application.score = score

                print(application.score)
            application.save()
            return redirect('employee-home')

    context = {
        'employee': employee,
        'jobs': jobs,
        'form': form,
        'form2': form2,
        'job': job,
        'person_type': person_type,





    }
    return render(request, 'employee/viewjob.html', context)

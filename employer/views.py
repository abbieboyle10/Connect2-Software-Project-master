from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
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
from account.models import Employer, Job, Employee
from .forms import JobForm, PersonForm


def employer_home(request):
    user = request.user

    context = {
        'user': user,


    }
    return render(request, 'employer/employer-home.html', context)


def employer_profile(request):

    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()

    context = {
        'employer': employer,
        'jobs': jobs,



    }

    return render(request, 'employer/profile.html', context)
    # return HttpResponse('Hello world')


def jobprofile(request, pk):
    employer = Employer.objects.get(user=request.user)

    jobs = Job.objects.filter(pk=pk)
    context = {
        'employer': employer,
        'jobs': jobs,



    }
    return render(request, 'employer/job_profile.html', context)


def jobs(request):

    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()

    context = {
        'employer': employer,
        'jobs': jobs,

    }

    return render(request, 'employer/jobs.html', context)
    # return HttpResponse('Hello world')


def browse(request):

    employer = Employer.objects.get(user=request.user)
    employees = Employee.objects.all()

    context = {
        'employer': employer,
        'employees': employees,

    }

    return render(request, 'employer/browse.html', context)
    # return HttpResponse('Hello world')


def createDes(request):

    form2 = PersonForm()
    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()

    context = {'employer': employer, 'jobs': jobs,
               }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form2 = PersonForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('employer-home'))

    context = {'form2': form2,
               }
    return render(request, 'employer/person_form.html', context)


def createJob(request):
    form = JobForm()
    form2 = PersonForm()
    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()

    context = {'employer': employer, 'jobs': jobs,
               }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('createDes'))

    context = {'form': form,
               }
    return render(request, 'employer/job_form.html', context)


def predictPerson(request):
    user = request.user
    print(request)
    if request.method == 'POST':
        temp = {}
        temp['content'] = request.POST.get('person_des')

    context = {
        'user': user,


    }
    return render(request, 'employer/employer-home.html', context)

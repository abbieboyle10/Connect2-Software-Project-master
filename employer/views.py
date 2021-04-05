from model_prediction import CustomModelPrediction
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
from .forms import JobForm, PersonForm, EmployerModelForm
import pickle
import os
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer


def employer_home(request):
    user = request.user

    context = {
        'user': user,


    }
    return render(request, 'employer/employer-home.html', context)


def employer_profile(request):

    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()
    form = EmployerModelForm(request.POST or None,
                             request.FILES or None, instance=employer)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'employer': employer,
        'jobs': jobs,
        'form': form,
        'confirm': confirm,



    }

    return render(request, 'employer/profile.html', context)
    # return HttpResponse('Hello world')


def jobprofile(request, pk):
    employer = Employer.objects.get(user=request.user)

    jobs = Job.objects.filter(pk=pk)
    test = Job.objects.get(pk=pk)
    applications = test.application_set.all()
    context = {
        'employer': employer,
        'jobs': jobs,
        'applications': applications,



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

    form2 = PersonForm()
    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()
    form = JobForm(request.POST or None,
                   request.FILES or None, instance=employer)

    context = {'employer': employer, 'jobs': jobs,
               }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = JobForm(request.POST)
        if form.is_valid():
            hiya = form.save(commit=False)
            hiya.employer = employer
            hiya.save()

            return HttpResponseRedirect(reverse('createDes'))

    context = {'form': form,
               }
    return render(request, 'employer/job_form.html', context)


def predictPerson(request):
    user = request.user
    print(request)

    if request.method == 'POST':
        sample = request.POST.get('description')
        test_requests = tuple([sample])
        print(test_requests)
    tags_split = [['sj'], ['sj'], ['nt'], ['nf'], ['sp'], ['nt'], ['sj'], ['nf'], ['sp'], ['sp'], ['sj'], ['sp'], ['sp'], ['nf'], ['nf'], ['sp'], ['sp'], ['sj'], ['nt'], ['nt'], ['sp'], [
        'sj'], ['sj'], ['sj'], ['sj'], ['nt'], ['sj'], ['nf'], ['nf'], ['nf'], ['nf'], ['sp'], ['nt'], ['sj'], ['nf'], ['nf'], ['sj'], ['sj'], ['sj'], ['nf'], ['nt'], ['sj'], ['nt'], ['nf']]
    tag_encoder = MultiLabelBinarizer()
    tag_encoded = tag_encoder.fit_transform(tags_split)
    num_tag = len(tag_encoded[0])

    classifier = CustomModelPrediction.from_path('.')
    results = classifier.predict(test_requests)
    print(results)

    for i in range(len(results)):
        print('Predicted labels:')
        for idx, val in enumerate(results[i]):
            if val > 0.6:
                print(tag_encoder.classes_[idx])
                personality = tag_encoder.classes_[idx]
                print(personality)
        print('\n')

    context = {
        'user': user,



    }
    return render(request, 'employer/employer-home.html', context)

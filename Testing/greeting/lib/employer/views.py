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
from account.filters import JobFilter

from account.decorators import employee_required, employee_check
from personality.models import Personality
from account.models import Employer, Job, Employee, MatchedSkills, Application, ConversationMessage, JobSkill, InterviewPlan, JobTag
from .forms import JobForm, EmployerModelForm, InterviewForm, JobSkillForm, JobTagForm
import pickle
import os
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from notifications.utilities import create_notification


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


def employerviewemp(request, xd, pl):
    application = Application.objects.get(pk=pl)
    employer = Employer.objects.get(user=request.user)
    employee = Employee.objects.get(pk=application.candidate.pk)
    personality = Personality.objects.get(employee=employee)
    print(employee)
    interviewdetails = InterviewPlan.objects.get(application=application)
    skills = employee.employeeskill_set.all()
    tags = employee.persontag_set.all()

    job = interviewdetails.application.job

    context = {
        'employer': employer,
        'employee': employee,
        'interviewdetails': interviewdetails,
        'personality': personality,
        'job': job,
        'skills': skills,
        'tags': tags

    }

    return render(request, 'employer/come.html', context)


def jobprofile(request, pk):
    employer = Employer.objects.get(user=request.user)

    jobs = Job.objects.filter(pk=pk)
    test = Job.objects.get(id=pk)
    applications = test.application_set.all().order_by('-score')
    print(applications)
    application = Application.objects.filter(job=test)

    context = {
        'employer': employer,
        'jobs': jobs,
        'applications': applications,

        'test': test,



    }
    return render(request, 'employer/test.html', context)


def jobviewer(request, pk):
    employer = Employer.objects.get(user=request.user)

    jobs = Job.objects.filter(pk=pk)
    test = Job.objects.get(id=pk)
    applications = test.application_set.all().order_by('-score')
    print(applications)
    application = Application.objects.filter(job=test)
    skills = test.jobskill_set.all()
    tags = test.jobtag_set.all()

    context = {
        'employer': employer,
        'jobs': jobs,
        'applications': applications,
        'skills': skills,
        'test': test,
        'tags': tags,



    }
    return render(request, 'employer/job_viewer.html', context)


def deleteApplication(request, pk):
    employer = Employer.objects.get(user=request.user)
    application = Application.objects.get(id=pk)
    jobs = employer.job_set.all()
    if request.method == "POST":
        application.delete()
        return HttpResponseRedirect(reverse('employer-home'))

    context = {'item': application,
               'jobs': jobs, }
    return render(request, 'employer/delete.html', context)


def likeview(request, pk, id):

    employer = Employer.objects.get(user=request.user)
    application = get_object_or_404(
        Application, id=request.POST.get('application_id'))
    job = Job.objects.get(pk=pk)
    print(job)
    if application.favourited == False:
        application.favourited = True
        application.save()
    else:
        application.favourited = False
        application.save()

    return HttpResponseRedirect(reverse('jobprofile', args=[int(pk)]))


def jobs(request):

    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()
    myFilter = JobFilter(request.GET, queryset=jobs)
    jobs = myFilter.qs

    context = {
        'employer': employer,
        'jobs': jobs,
        'myFilter': myFilter,

    }

    return render(request, 'employer/jobs.html', context)
    # return HttpResponse('Hello world')


def clearjobs(request):

    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()
    myFilter = JobFilter(request.GET, queryset=jobs)

    context = {
        'employer': employer,
        'jobs': jobs,
        'myFilter': myFilter,

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

    form2 = EmployerModelForm()
    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()

    context = {'employer': employer, 'jobs': jobs,
               }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form2 = EmployerModelForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse('employer-home'))

    context = {'form2': form2,

               }
    return render(request, 'employer/person_form.html', context)


def createJob(request):
    user = request.user
    form2 = EmployerModelForm()
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
            hiya.status = "Open"
            sample = request.POST.get('description_personality')
            test_requests = tuple([sample])
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
                hiya.ideal_person = personality

                hiya.save()
                context = {
                    'user': user,



                }

                if personality == "nt":
                    print(personality)
                    return render(request, 'employer/job-nt.html', context)
                elif personality == "nf":
                    return render(request, 'employer/job-nf.html', context)
                elif personality == 'sp':
                    return render(request, 'employer/job-sp.html', context)
                else:
                    return render(request, 'employer/job-sj.html', context)

    context = {'form': form,
               }
    return render(request, 'employer/job_form.html', context)


def nextround(request, pk):
    job = Job.objects.get(pk=pk)
    print(job)
    applications = job.application_set.all()
    for application in applications:
        if application.favourited == False:
            application.delete()
        else:
            application.job_round += 1
            job.job_round += 1
            job.save()
            application.save()

    return HttpResponseRedirect(reverse('jobprofile', args=[int(pk)]))


def closejob(request, pk):
    job = Job.objects.get(pk=pk)
    job.status = 'Closed'
    employer = Employer.objects.get(user=request.user)
    jobs = employer.job_set.all()
    job.save()
    context = {
        'jobs': jobs,
        'employer': employer,
    }
    return render(request, 'employer/jobs.html', context)


def createInterview(request, pk):
    job = Job.objects.get(pk=pk)
    job.status = 'Interview'
    employer = Employer.objects.get(user=request.user)
    applications = job.application_set.all()
    content = "Congratulations, you have been selected for an interview at " + \
        str(employer)+" please await further details."
    print(content)
    for application in applications:
        if application.favourited == True:
            conversationmessage = ConversationMessage.objects.create(
                application=application, content=content, created_by=request.user)
            create_notification(request, application.candidate.user, application.job, application,
                                'message', extra_id=application.id)
            application.interview = True

            print(application.interview)
            application.save()
        else:
            application.delete()

    jobs = employer.job_set.all()
    job.save()
    context = {
        'jobs': jobs,
        'employer': employer,
    }
    return HttpResponseRedirect(reverse('jobprofile', args=[int(pk)]))


def scheduleInterview(request, id, pk):
    job = Job.objects.get(pk=pk)
    application = Application.objects.get(id=id)
    form = InterviewForm(request.POST or None,
                         request.FILES or None, instance=application)

    context = {
        'application': application,
        'form': form,
    }
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = InterviewForm(request.POST)
        if form.is_valid():
            hiya = form.save(commit=False)
            hiya.application = application
            hiya.confirmed = True
            application.interview = False
            application.status = 'Interview'
            print(application.status)
            content = "Your interview for "+str(job)+" has been scheduled for "+str(hiya.date)+" at " + str(hiya.time)+". It will be an "+str(hiya.location) + \
                " interview taking place at "+str(hiya.platform)
            conversationmessage = ConversationMessage.objects.create(
                application=application, content=content, created_by=request.user)
            application.save()
            hiya.save()
            return HttpResponseRedirect(reverse('jobprofile', args=[int(pk)]))
    return render(request, 'employer/schedule.html', context)


def createJobSkill(request, pk):
    form = JobSkillForm()
    employer = Employer.objects.get(user=request.user)
    job = Job.objects.get(pk=pk)
    skill = JobSkill.objects.filter(job=job)
    skills = job.jobskill_set.all()

    context = {'employer': employer, 'job': job,
               'skill': skill, 'skills': skills, 'form': form}

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = JobSkillForm(request.POST)
        if form.is_valid():
            hiya = form.save()
            hiya.job = job
            hiya.save()
            return HttpResponseRedirect(reverse('createJobSkill', args=[int(pk)]))

    context = {'employer': employer, 'job': job,
               'skill': skill, 'skills': skills, 'form': form}
    return render(request, 'employer/job_skill.html', context)


def createJobtag(request, pk):
    form = JobTagForm()
    employer = Employer.objects.get(user=request.user)
    job = Job.objects.get(pk=pk)
    tag = JobTag.objects.filter(job=job)
    tags = job.jobtag_set.all()

    context = {'employer': employer, 'job': job,
               'tag': tag, 'tags': tags, 'form': form}

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = JobTagForm(request.POST)
        if form.is_valid():
            hiya = form.save()
            hiya.job = job
            hiya.save()
            return HttpResponseRedirect(reverse('createJobtag', args=[int(pk)]))

    context = {'employer': employer, 'job': job,
               'tag': tag, 'tags': tags, 'form': form}
    return render(request, 'employer/job_tag.html', context)

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from account.decorators import employee_required, employee_check
from account.models import Employee, EmployeeSkill, Job, JobTag, JobSkill, LTM, LocationTag, MatchedSkills, PersonTag, Application, User, ConversationMessage, InterviewPlan, JobRankings,  SharedThing
from .forms import SkillForm, ExperienceForm
from django.contrib.auth.decorators import user_passes_test
from personality.models import Quiz, Result, Personality
from .forms import EmployeeModelForm, ApplyJobForm, TagForm
from notifications.utilities import create_notification
from account.filters import JobFilter2
from collections import Counter


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
    tags = employee.persontag_set.all()
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
        'tags': tags


    }

    return render(request, 'employee/emp_profile.html', context)


@user_passes_test(employee_check, login_url='jobs')
def personality_page(request):

    return render(request, 'employee/personality.html')


def getrandom():
    return PersonTag.objects.filter(employee=employee).order_by("?").first()


@user_passes_test(employee_check, login_url='jobs')
def find_job(request):

    employee = Employee.objects.get(user=request.user)
    jobs = Job.objects.all()
    myFilter = JobFilter2(request.GET, queryset=jobs)
    jop = myFilter.qs
    personality = Personality.objects.get(employee=employee)
    jobrankingz = JobRankings.objects.filter(
        employee=employee)
    shares = SharedThing.objects.filter(
        employee=employee)
    if shares:
        shares.delete()
    ltm = LTM.objects.filter(employee=employee)
    ltm.delete()
    ltm = LocationTag.objects.filter(employee=employee)
    ltm.delete()
    jobloc = LocationTag.objects.filter(employee=employee)
    jobloc.delete()
    jobrankingz.delete()
    print(personality)
    context = {'jobs': jobs, 'personality': personality,
               'myFilter': myFilter}
    for job in jobs:
        if job.status == 'Open':
            jobrank = JobRankings.objects.filter(job=job)
            if jobrank:
                jobrank.delete()
            jobrank = JobRankings.objects.create(
                job=job, score=0, employee=employee)

            jobskills = job.jobskill_set.all().values_list('title', flat=True).distinct()
            employeeskills = employee.employeeskill_set.all().values_list('title',
                                                                          flat=True).distinct()

            jobtags = job.jobskill_set.all().values_list('title', flat=True).distinct()
            employeetags = employee.employeeskill_set.all().values_list('title',
                                                                        flat=True).distinct()
            employeeskills_as_set = set(employeeskills)
            employeetags_as_set = set(employeetags)
            intersection = employeeskills_as_set.intersection(jobskills)
            intersection2 = employeetags_as_set.intersection(jobtags)
            intersection_as_list = list(intersection)
            intersection_as_list2 = list(intersection2)

            matched_amount = len(intersection_as_list+intersection_as_list2)/2
            score = matched_amount
            if job.ideal_person == personality.group:
                score += 1
            else:
                hscore = 0
            for x in intersection_as_list:
                score += 1
                SharedThing.objects.create(
                    title=x, jobrank=jobrank, sort="Skill", employee=employee)
            jobrank.score = score
            jobrank.save()
    checker = 0
    jl = 0

    jobrankings = JobRankings.objects.filter(
        job=job).order_by('-score')
    print(jobrankings)
    p = 0
    checker = 0
    for l in jobrankings:
        checker = checker+1
        if checker < 3:
            l.topthree = True
            l.save()
        else:
            p = 0

    topthree = JobRankings.objects.filter(
        employee=employee).order_by('-score')[:3]
    sharedthings = SharedThing.objects.filter(
        jobrank__in=JobRankings.objects.filter(employee=employee))

    city = employee.city
    score = 0
    jobtags = JobTag.objects.all()

    persontags = PersonTag.objects.filter(employee=employee)
    matchedtags = []
    for j in jobtags:
        if j.job.city == city:
            for n in persontags:

                if j.title == n.title:
                    matchedtags.append(n.title)
                    print(matchedtags)

                    p = LocationTag.objects.create(
                        job=j.job, employee=employee, tag=j.title)

            hi = Counter(matchedtags)

    most_common_element = hi.most_common(1)

    key = most_common_element[0]

    hi = key[0]

    lmn = LTM.objects.create(
        employee=employee, city=city, tag=hi)
    lmn = LTM.objects.get(employee=employee)
    areatags = LocationTag.objects.filter(tag=hi).order_by("?")[:3]

    print(areatags)
    context = {'jobs': jobs, 'jop': jop, 'personality': personality,
               'myFilter': myFilter, 'topthree': topthree, 'sharedthings': sharedthings, 'lmn': lmn, 'areatags': areatags}
    return render(request, 'employee/findjob.html', context)


def clearjobs2(request):

    employee = Employee.objects.get(user=request.user)
    jobs = Job.objects.all()
    myFilter = JobFilter2(request.GET, queryset=jobs)
    jobs = myFilter.qs

    context = {
        'employee': employee,
        'jobs': jobs,
        'myFilter': myFilter,

    }

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
            hiya = form.save()
            hiya.employee = employee
            hiya.save()

            return HttpResponseRedirect(reverse('createskill'))

    context = {'form': form, 'employee': employee, 'skills': skills,
               'experiences': experiences}
    return render(request, 'employee/skills_form.html', context)


def createTag(request):
    form = TagForm()
    employee = Employee.objects.get(user=request.user)
    tags = employee.persontag_set.all()
    skills = employee.employeeskill_set.all()
    experiences = employee.experience_set.all()
    context = {'employee': employee, 'tags': tags,
               'experiences': experiences, }

    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = TagForm(request.POST)
        if form.is_valid():
            hiya = form.save()
            hiya.employee = employee
            hiya.save()
            print(hiya)
            return HttpResponseRedirect(reverse('createtag'))

    context = {'form': form, 'employee': employee, 'tags': tags,
               'experiences': experiences}
    return render(request, 'employee/tag_form.html', context)


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
            return HttpResponseRedirect(reverse('createexperience'))

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
    skills = JobSkill.objects.filter(job=job)
    tags = JobTag.objects.filter(job=job)
    personality = Personality.objects.get(employee=employee)
    employeeskills = employee.employeeskill_set.all().values_list('title',
                                                                  flat=True).distinct()
    print(employeeskills)
    jobskills = job.jobskill_set.all().values_list('title', flat=True).distinct()
    print(jobskills)
    employeeskills_as_set = set(employeeskills)
    print(employeeskills_as_set)
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
            app = application
            job.no_applicants = job.no_applicants+1
            print(job.no_applicants)
            job.save()
            create_notification(request, job.employer.user, application.job, app,
                                'application', extra_id=application.id)

            application.save()
            score = 0
            print(job_type)
            print(person_type)
            if job_type == person_type:

                application.match = True
                score += 5

            else:

                application.match = False

            for x in intersection_as_list:
                MatchedSkills.objects.create(application=application, title=x)

                score += 1
                application.score = score

                print(application.score)
            application.save()
            return redirect('employee-home')
        print(skills)

    context = {
        'employee': employee,
        'jobs': jobs,
        'form': form,
        'form2': form2,
        'job': job,
        'person_type': person_type,
        'skills': skills,
        'tags': tags,
        'personality': 'personality'





    }
    return render(request, 'employee/viewjob.html', context)


def employee_applications(request):

    employee = Employee.objects.get(user=request.user)

    applications = Application.objects.filter(candidate=employee)
    context = {
        'employee': employee,
        'applications': applications
    }
    return render(request, 'employee/applications.html', context)


def view_application(request, id, pk):
    app = get_object_or_404(
        Application, id=id)
    employee = Employee.objects.filter(pk=app.candidate.pk)
    print(employee)

    print(employee)
    user = request.user
    test = Job.objects.get(pk=pk)
    context = {

        'app': app,
        'test': test,
        'employee': employee
    }

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(
                application=app, content=content, created_by=request.user)
            if request.user.is_employee == True:
                create_notification(request, test.employer.user, app.job, app,
                                    'message', extra_id=app.id)
                print("employee")
            else:
                create_notification(request, app.candidate.user, app.job, app,
                                    'message', extra_id=app.id)
                print("employer")

            return redirect('view_application', id=app.id, pk=test.pk)
    if app.status == "Interview" or "Accepted" or "Rejected":
        interviewdetails = InterviewPlan.objects.filter(application=app)

        context = {
            'interviewdetails': interviewdetails,
            'app': app,
            'test': test,
            'employee': employee
        }

    if request.user.is_employer:
        return render(request, 'employer/message.html', context)
    else:
        return render(request, 'employee/message.html', context)


def AcceptInterview(request, id, pk):
    app = get_object_or_404(
        Application, id=id)
    app.status = "Accepted"
    test = Job.objects.get(pk=pk)
    app.save()
    content = "The candidate has accepeted your interview request. You now have access to their user profile."
    conversationmessage = ConversationMessage.objects.create(
        application=app, content=content, created_by=request.user)
    create_notification(request, app.job.employer.user, app.job, app,
                        'message', extra_id=app.id)
    context = {
        'app': app,
        'test': test
    }
    return HttpResponseRedirect(reverse('view_application', args=[int(id), int(pk)]))


def RejectInterview(request, pk, id):
    app = get_object_or_404(
        Application, id=id)
    app.status = "Rejected"
    app.save()
    content = "The candidate has rejected your interview request."
    conversationmessage = ConversationMessage.objects.create(
        application=app, content=content, created_by=request.user)
    create_notification(request, app.job.employer.user, app.job, app,
                        'message', extra_id=app.id)
    context = {
        'app': app
    }
    return HttpResponseRedirect(reverse('view_application', args=[int(id), int(pk)]))

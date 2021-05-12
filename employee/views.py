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
from account.models import Employee, EmployeeSkill, Job, MatchedSkills, Application, User, ConversationMessage, InterviewPlan, JobRankings, TopThree, SharedThing
from .forms import SkillForm, ExperienceForm
from django.contrib.auth.decorators import user_passes_test
from personality.models import Quiz, Result, Personality
from .forms import EmployeeModelForm, ApplyJobForm, TagForm
from notifications.utilities import create_notification
from account.filters import JobFilter2


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


@user_passes_test(employee_check, login_url='jobs')
def find_job(request):
    employee = Employee.objects.get(user=request.user)
    jobs = Job.objects.all()
    myFilter = JobFilter2(request.GET, queryset=jobs)
    jobs = myFilter.qs
    personality = Personality.objects.get(employee=employee)
    print(personality)
    context = {'jobs': jobs, 'personality': personality,
               'myFilter': myFilter}
    for job in jobs:
        if job.status == 'Open':
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
            matched_amount = len(intersection_as_list+intersection_as_list2)
            score = matched_amount
            if job.ideal_person == personality.group:
                score += 1
            else:
                hscore = 0
            JobRankings.objects.create(job=job, score=score, employee=employee)
    jobrankings = JobRankings.objects.filter(
        employee=employee).order_by('-score')
    jobrankings_as_list = list(jobrankings)
    checker = 0
    for x in jobrankings:
        checker = checker+1
        if checker < 4:
            print(x.score)
            jobskills = x.job.jobskill_set.all().values_list('title', flat=True).distinct()
            employeeskills = employee.employeeskill_set.all().values_list('title',
                                                                          flat=True).distinct()
            jobtags = x.job.jobskill_set.all().values_list('title', flat=True).distinct()
            employeetags = employee.employeeskill_set.all().values_list('title',
                                                                        flat=True).distinct()
            employeeskills_as_set = set(employeeskills)
            employeetags_as_set = set(employeetags)
            intersection = employeeskills_as_set.intersection(jobskills)
            intersection2 = employeetags_as_set.intersection(jobtags)
            for c in intersection:
                toll = SharedThing.objects.filter(
                    employee=employee)
                if toll:
                    toll.delete()
                SharedThing.objects.create(
                    title=c.title, jobrank=x, sort="Skill", employee=employee)
            for c in intersection2:
                SharedThing.objects.create(
                    title=c.title, jobrank=x, sort="Tag", employee=employee)
            lol = TopThree.objects.filter(
                employee=employee)
            if lol:
                lol.delete()
            TopThree.objects.create(jobranking=x, employee=employee)
        else:
            x.delete()

    context = {'jobs': jobs, 'personality': personality,
               'myFilter': myFilter}
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
        interviewdetails = InterviewPlan.objects.get(application=app)

        print(interviewdetails.pk)

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

from django.urls import path
from django.conf.urls import url
from . import views

from .views import employee_home, employee_profile, personality_page, find_job, createSkill, createExperience, viewjob, view_application, employee_applications, AcceptInterview, RejectInterview, clearjobs2, createTag

import employee

urlpatterns = [

    path('employee-home/', employee_home, name='employee-home'),
    path('employee-profile/',
         employee_profile, name='employee-profile'),
    path('personality/', personality_page, name='personality-page'),
    path('employee_applications/', employee_applications,
         name='employee_applications'),
    path('findjob/', find_job, name='findjob'),
    path('clearjobs2/', clearjobs2, name='clearjobs2'),
    path('createskill/', createSkill, name='createskill'),
    path('createtag/', createTag, name='createtag'),
    path('acceptinterview/<int:id>/<int:pk>/',
         AcceptInterview, name='acceptinterview'),
    path('rejectinterview/<int:id>/<int:pk>/',
         RejectInterview, name='rejectinterview'),

    path('createexperience/', createExperience, name='createexperience'),
    path('<int:pk>/view', viewjob, name='viewjob'),
    path('application/<int:id>/<int:pk>/',
         view_application, name='view_application'),
]

# path('createskill/employee/profile',
#    employee_profile, name='employee-profile'),

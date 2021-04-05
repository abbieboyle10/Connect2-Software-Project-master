from django.urls import path
from django.conf.urls import url
from . import views

from .views import employer_home, employer_profile, jobs, browse, createJob, jobprofile, predictPerson, createDes

import employer

urlpatterns = [

    path('employer-home/', employer_home, name='employer-home'),
    path('employer-profile/', employer_profile, name='employer-profile'),
    path('jobs/', jobs, name='jobs'),
    path('browse/', browse, name='browse'),
    path('createjob/', createJob, name='createjob'),
    path('createDes/', createDes, name='createDes'),
    path('<int:pk>/profile', jobprofile, name='jobprofile'),
    path('createDes/predictPerson',
         predictPerson, name='predictPerson'),






]

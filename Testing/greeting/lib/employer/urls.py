import employer
from django.urls import path
from django.conf.urls import url
from . import views

from .views import employer_home, employer_profile, jobs, browse, createJob, jobprofile, createDes, deleteApplication, likeview, nextround, closejob, createInterview, scheduleInterview, createJobSkill, clearjobs, jobviewer, employerviewemp, createJobtag


urlpatterns = [

    path('employer-home/', employer_home, name='employer-home'),
    path('employer-profile/', employer_profile, name='employer-profile'),
    path('jobs/', jobs, name='jobs'),
    path('jobs/', clearjobs, name='clearjobs'),

    path('browse/', browse, name='browse'),
    path('createjob/', createJob, name='createjob'),
    path('<int:pk>/createjobskill/', createJobSkill, name='createJobSkill'),
    path('<int:pk>/createjobtag/', createJobtag, name='createJobtag'),
    path('createDes/', createDes, name='createDes'),
    path('<int:pk>/profile', jobprofile, name='jobprofile'),
    path('<int:xd>/<int:pl>/employerviewemp',
         employerviewemp, name='gotopage'),
    path('<int:pk>/<int:id>/scheduleInterview',
         scheduleInterview, name='scheduleInterview'),
    path('<int:pk>/round', nextround, name='nextround'),
    path('<int:pk>/closejob', closejob, name='closejob'),
    path('<int:pk>/jobviewer', jobviewer, name='jobviewer'),
    path('<int:pk>/createInterview', createInterview, name='createInterview'),
    path('like/<int:pk>/<int:id>/', likeview, name='likeview'),

    path('delete_order/<str:pk>/', views.deleteApplication,
         name="delete_application"),








]

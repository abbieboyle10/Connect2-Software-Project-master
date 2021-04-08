import employer
from django.urls import path
from django.conf.urls import url
from . import views

from .views import employer_home, employer_profile, jobs, browse, createJob, jobprofile, predictPerson, createDes, deleteApplication, likeview


urlpatterns = [

    path('employer-home/', employer_home, name='employer-home'),
    path('employer-profile/', employer_profile, name='employer-profile'),
    path('jobs/', jobs, name='jobs'),
    path('browse/', browse, name='browse'),
    path('createjob/', createJob, name='createjob'),
    path('createDes/', createDes, name='createDes'),
    path('<int:pk>/profile', jobprofile, name='jobprofile'),
    path('like/<int:pk>/<int:id>/', likeview, name='likeview'),
    path('createDes/predictPerson',
         predictPerson, name='predictPerson'),
    path('delete_order/<str:pk>/', views.deleteApplication,
         name="delete_application"),







]

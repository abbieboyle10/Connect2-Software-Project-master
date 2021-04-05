from django.urls import path, re_path
from .views import *


urlpatterns = [

    path('mbti/', QuizListView.as_view(), name='quiz'),
    path('<int:pk>/', quiz_view, name='quiz-home'),
    path('<int:pk>/save/', save_quiz_view, name='save-quiz'),
    path('<int:pk>/data/', quiz_data_view, name='quiz-data-home'),

]

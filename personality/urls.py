from django.urls import path, re_path
from .views import *


urlpatterns = [

    path('mbti/', QuizListView.as_view(), name='quiz'),
    path('<pk>/', quiz_view, name='quiz-home'),
    path('<pk>/save/', save_quiz_view, name='save-quiz'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-home'),

]

from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from account.models import *
import random


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    letters_types = (
        ('e', 'e'),
        ('i', 'i'),
        ('n', 'n'),
        ('s', 's'),
        ('f', 'f'),
        ('t', 't'),
        ('j', 'j'),
        ('p', 'p'),

    )
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=200, blank=True, choices=letters_types)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    e_score = models.FloatField()
    i_score = models.FloatField()
    n_score = models.FloatField()
    s_score = models.FloatField()
    t_score = models.FloatField()
    f_score = models.FloatField()
    p_score = models.FloatField()
    j_score = models.FloatField()

    def __str__(self):
        return str(self.pk)


class Personality(models.Model):
    personality_groups = {
        ('nt', 'nt'),
        ('nf', 'nf'),
        ('sj', 'sj'),
        ('sp', 'sp'),
    }
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_letter = models.CharField(max_length=200)
    second_letter = models.CharField(max_length=200)
    third_letter = models.CharField(max_length=200)
    fourth_letter = models.CharField(max_length=200)
    person_type = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    group = models.CharField(max_length=200, null=True,
                             choices=personality_groups)

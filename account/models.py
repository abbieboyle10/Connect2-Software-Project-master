from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from .utils import get_random_code
from django.template.defaultfilters import slugify
from django.db.models import Q

# Create your models here.


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)
    tag = models.TextField(max_length=200, blank=True)
    sector = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.jpg', upload_to='avatar_pics')
    county = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    personality_test = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}-{self.created}"

    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug == "":
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) +
                                  " " + str(self.last_name))
                ex = Employee.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Employee.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


class Tag(models.Model):

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill_level = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    years_of = (
        ('1 year <', '1 year <'),
        ('1 - 2 years', '1 - 2 years'),
        ('2 - 5 years', '2 - 5 years'),
        ('5 - 10 years', '5 - 10 years'),
        ('10+ years', '10+ years'),


    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE)
    level = models.CharField(max_length=200, blank=False, choices=skill_level)
    years_of = models.CharField(max_length=200, blank=True, choices=years_of)
    description = models.TextField(max_length=400, blank=True)

    def __str__(self):
        return str(self.tag)


class Experience(models.Model):
    length = (
        ('1 year <', '1 year <'),
        ('1 - 2 years', '1 - 2 years'),
        ('2 - 5 years', '2 - 5 years'),
        ('5 - 10 years', '5 - 10 years'),
        ('10+ years', '10+ years'),
    )

    currently = (
        ('Yes', 'Yes'),
        ('No', 'No'),


    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE)

    role = models.CharField(max_length=200, blank=False)
    current = models.CharField(
        max_length=200, blank=False, choices=currently, default='No')
    description = models.TextField(max_length=400, blank=True)
    time_in_role = models.CharField(
        max_length=200, blank=False, choices=length)

    def __str__(self):
        return self.role


class Employer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    sector = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.jpg', upload_to='avatar_pics')
    county = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


__initial_company_name = None


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__initial_company_name = self.company_name

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if self.company_name != self.__initial_company_name:
            if self.company_name:
                to_slug = slugify(str(self.company_name))
                ex = Employer.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Employer.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


class Job(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),

    )
    CONTRACT = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),

    )

    WORK = (
        ('Office', 'Office'),
        ('Remote', 'Remote'),

    )
    LENGTH = (
        ('Permanent', 'Permanent'),
        ('Temporary', 'Temporary'),

    )

    employer = models.ForeignKey(
        Employer, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    title = models.CharField(max_length=200)
    description_role = models.TextField(max_length=2000, null=True, blank=True)
    description_personality = models.CharField(
        max_length=200, null=True, blank=True)
    contract = models.CharField(max_length=200, null=True, choices=CONTRACT)
    office_type = models.CharField(max_length=200, null=True, choices=WORK)
    length = models.CharField(max_length=200, null=True, choices=LENGTH)
    ideal_person = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    num_hires = models.IntegerField(null=True)

# need to add skill list!

    def __str__(self):
        return self.title


class Person_Des(models.Model):

    Job = models.ForeignKey(
        Job, null=True, on_delete=models.CASCADE)
    description = models.CharField(
        max_length=2000, null=True, blank=True)
    enviornment = models.CharField(
        max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.description


class Application(models.Model):
    STATUS = {
        ('applied', 'applied'),
        ('second round', 'second round'),
        ('interview', 'interview'),
        ('rejected', 'rejected'),
    }
    candidate = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='candidates')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True)
    cover_letter = models.TextField(
        null=True)

    def __str__(self):
        return f"{self.candidate}-{self.job}-{self.status}"

from django.contrib import admin
from .models import User, Employee, Employer, Job, Skill, Tag, Experience, Person_Des, Application
# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Tag)
admin.site.register(Experience)
admin.site.register(Person_Des)
admin.site.register(Application)

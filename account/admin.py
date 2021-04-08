from django.contrib import admin
from .models import User, Employee, Employer, Job, EmployeeSkill, JobSkill, Experience, Application, MatchedSkills
# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(JobSkill)
admin.site.register(EmployeeSkill)
admin.site.register(Experience)
admin.site.register(Application)
admin.site.register(MatchedSkills)

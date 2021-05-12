from django.contrib import admin
from .models import User, Employee, Employer, Job, EmployeeSkill, JobSkill, Experience, Application, MatchedSkills, InterviewPlan, ConversationMessage, JobRankings, SharedThing
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
admin.site.register(InterviewPlan)
admin.site.register(ConversationMessage)
admin.site.register(JobRankings)
admin.site.register(SharedThing)

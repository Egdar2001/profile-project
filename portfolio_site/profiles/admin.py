from django.contrib import admin
from .models import UserProfile, Project, Education, WorkExperience, Certification

admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Certification)

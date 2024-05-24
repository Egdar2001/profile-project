from django import forms
from .models import UserProfile, Project, Education, WorkExperience, Certification

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'skills', 'contact_details']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_date', 'end_date']

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['company', 'position', 'start_date', 'end_date']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'institution', 'date_obtained']

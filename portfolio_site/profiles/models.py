from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    contact_details = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Education(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class WorkExperience(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Certification(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    date_obtained = models.DateField()

    def __str__(self):
        return f"{self.name} from {self.institution}"

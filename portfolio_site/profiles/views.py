from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ProjectForm, EducationForm, WorkExperienceForm, CertificationForm
from .models import Project, Education, WorkExperience, Certification

def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile if request.user.is_authenticated else None)
        if form.is_valid():
            if request.user.is_authenticated:
                form.save()
                return redirect('profile')
            else:
                return redirect('add_profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile if request.user.is_authenticated else None)
    return render(request, 'profiles/edit_profile.html', {'form': form})

def profile(request):
    user_profile = request.user.userprofile if request.user.is_authenticated else None
    projects = Project.objects.filter(user_profile=user_profile) if user_profile else []
    education = Education.objects.filter(user_profile=user_profile) if user_profile else []
    work_experience = WorkExperience.objects.filter(user_profile=user_profile) if user_profile else []
    certifications = Certification.objects.filter(user_profile=user_profile) if user_profile else []
    context = {
        'user_profile': user_profile,
        'projects': projects,
        'education': education,
        'work_experience': work_experience,
        'certifications': certifications
    }
    return render(request, 'profiles/profile.html', context)

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            if request.user.is_authenticated:
                project.user_profile = request.user.userprofile
            project.save()
            return redirect('profile')
    else:
        form = ProjectForm()
    return render(request, 'profiles/add_project.html', {'form': form})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'profiles/project_detail.html', {'project': project})

def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            if request.user.is_authenticated:
                education.user_profile = request.user.userprofile
            education.save()
            return redirect('profile')
    else:
        form = EducationForm()
    return render(request, 'profiles/add_education.html', {'form': form})

def add_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            if request.user.is_authenticated:
                work_experience.user_profile = request.user.userprofile
            work_experience.save()
            return redirect('profile')
    else:
        form = WorkExperienceForm()
    return render(request, 'profiles/add_work_experience.html', {'form': form})

def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            if request.user.is_authenticated:
                certification.user_profile = request.user.userprofile
            certification.save()
            return redirect('profile')
    else:
        form = CertificationForm()
    return render(request, 'profiles/add_certification.html', {'form': form})

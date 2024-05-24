from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('project/add/', views.add_project, name='add_project'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('education/add/', views.add_education, name='add_education'),
    path('work_experience/add/', views.add_work_experience, name='add_work_experience'),
    path('certification/add/', views.add_certification, name='add_certification'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('experience/', views.experience, name='experience'),
    path('subExp/', views.subject_experience, name='subExp'),
    path('paperpublications/', views.paper, name='paper'),
    path('FoundedProject/', views.founded, name='founded'),
    path('Seminars/', views.seminar, name='seminar'),
    path('Events/', views.event, name='event'),
    path('Talks/', views.invited, name='invited'),
    path('Roles/', views.roles, name='roles'),
    path('Conference/', views.conference, name='conference'),
    path('Others/', views.others, name='others'),
]
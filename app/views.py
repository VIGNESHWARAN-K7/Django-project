from django.shortcuts import render
from app.models import *
# Create your views here.
def index(request):
    home=Home.objects.all()
    return render(request, 'index.html',{"home":home})

def profile(request):
    profile=Profile.objects.all()
    image=Images.objects.all()
    return render(request, 'others/profile.html',{"profile":profile, "image":image})


def experience(request):
    experience=Experience.objects.all()
    return render(request, 'others/experience.html',{"experience":experience})

def subject_experience(request):
    sub_exp=Subject_experience.objects.all()
    return render(request, 'others/subject_experience.html',{"subExp":sub_exp})


def paper(request):
    paper=Paper.objects.all()
    return render(request, 'others/paper.html',{"paper":paper})

def founded(request):
    founded=FoundedProject.objects.all()
    return render(request, 'others/founded.html',{"founded":founded})
# 

def seminar(request):
    seminar=Seminars.objects.all()
    return render(request, 'others/seminars.html',{"seminar":seminar})
def event(request):
    event=Eventorganized.objects.all()
    return render(request, 'others/events.html',{"event":event})
def invited(request):
    invited=InvitedTalks.objects.all()
    return render(request, 'others/invited.html',{"invited":invited})
def roles(request):
    roles=Roles.objects.all()
    return render(request, 'others/roles.html',{"roles":roles})
def conference(request):
    conference=Conferences.objects.all()
    return render(request, 'others/conference.html',{"conference":conference})

def others(request):
    return render(request, 'others/others.html')
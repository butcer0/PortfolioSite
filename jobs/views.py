from django.shortcuts import render

from .models import Job


def home(request):
    jobs = Job.objects  # this gets every job and turns them into objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

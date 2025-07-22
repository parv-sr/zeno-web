from django.shortcuts import render
from bookings.models import Subject

def home_view(request):
    return render(request, 'home.html')


def about_us_view(request):
    subjects = Subject.objects.all()
    return render(request, 'about_us.html', {'subjects':subjects})
from django.shortcuts import render
from bookings.models import Subject

def home_view(request):
    return render(request, 'home.html')


def about_us_view(request):
    subjects = Subject.objects.all()

    subject_icon_map = {
        "Math (inclusive of mechanics, pure math and statistics) (8-12)": "Maths.svg",
        "Business (9-12)": "Business 2.svg",
        "IGCSE EFL and FLE (9-10)": "FLE_ESL.svg",
        "Environmental science (9-12)": "EVM.svg",
        "EGP": "EGP.svg",
        "Biology (8-12)": "Biology.svg",
        "Economics (9-12)": "Econ.svg",
        "Chemistry (8-12)": "Chemistry.svg",
        "Physics (8-12)": "Physics.svg",
    }

    return render(request, 'about_us.html', {
        'subjects':subjects,
        "subject_icons": subject_icon_map,
        })

def code_of_conduct(request):
    return render(request, 'code_of_conduct.html')


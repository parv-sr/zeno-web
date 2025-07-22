from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookings.models import Booking, BookingClaimLog
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from .models import TeacherProfile
from bookings.models import Subject
from django.http import JsonResponse
from datetime import date

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if hasattr(user, 'teacherprofile') and user.teacherprofile.is_teacher:
                login(request, user)
                return redirect('teacher_dashboard')
            else:
                messages.error(request, "You are not authorised as a teacher.")
        else:
            messages.error(request, "Invalid credentials")

    return render(request, "users/login.html")

@login_required
def teacher_dashboard(request):

    teacher_subjects = request.user.teacherprofile.subjects.all()

    new_requests = Booking.objects.filter(
        claimed_by__isnull=True,
        subject__in=teacher_subjects
    ).order_by('preferred_date')

    my_classes = Booking.objects.filter(
        claimed_by=request.user
    ).order_by('preferred_date')

    print("Teacher:", request.user)
    print("Subjects:", list(teacher_subjects))
    print("Available Bookings:", list(new_requests))


    bookings = Booking.objects.all().order_by('-timestamp')
    return render(request, "users/dashboard.html", {
        'bookings' : bookings,
        'new_requests' : new_requests,
        'my_classes' : my_classes,
        })


@require_POST
@login_required
def claim_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.user.teacherprofile.subjects.filter(id=booking.subject.id).exists() and not booking.claimed_by:
        booking.claimed_by = request.user
        booking.save()
    BookingClaimLog.objects.create(
        booking=booking,
        claimed_by = request.user
    )
    return redirect('teacher_dashboard')

def tutor_list(request):
    subject_id = request.GET.get('subject')
    subjects = Subject.objects.all()

    if subject_id:
        tutors = TeacherProfile.objects.filter(subjects__id=subject_id)
    else:
        tutors = TeacherProfile.objects.all()

    return render(request, 'users/tutors.html', {
        'tutors': tutors,
        'subjects': subjects,
        'selected_subject': int(subject_id) if subject_id else None,
    })


SUBJECT_COLOR_MAP = {
    'Math (inclusive of mechanics, pure math and statistics) (8-12)': '#4C5FD5',
    'Computer science (9-12)': '#00BFA6',
    'Business (9-12)': '#F57C00',
    'IGCSE EFL and FLE (9-10)': '#8E24AA',
    'General English (AS/A)': '#5E35B1',
    'Environmental science (9-12)': '#43A047',
    'EGP': '#1E88E5',
    'Biology (8-12)': '#43A047',
    'Economics (9-12)': '#F9A825',
    'Chemistry (8-12)': '#E53935',
    'Physics (8-12)': '#3949AB',
    'ICT (9-12)': '#6D4C41',
    'Accountancy (9-12)': '#FF7043',
    'Psychology (11-12)': '#D81B60',
    'IPQ (11-12)': '#0097A7',
    'Sociology (9-12)': '#7E57C2',
}


@login_required
def teacher_calendar_events(request):
    try:
        profile = request.user.teacherprofile
    except TeacherProfile.DoesNotExist:
        return JsonResponse([], safe=False)
        

    teacher_subjects = request.user.teacherprofile.subjects.all()

    today = date.today()
    events = []
    bookings = Booking.objects.filter(
        subject__in=teacher_subjects,
        claimed_by = request.user,
        )
    

    for booking in bookings:
        is_past = booking.preferred_date < today

        base_color = SUBJECT_COLOR_MAP.get(str(booking.subject), '#03BBD0')
        color = '#e0e0e0' if is_past else base_color

        events.append({
            'id': booking.id,
            'title': f"{booking.full_name}",
            'start': str(booking.preferred_date),
            'backgroundColor': color,
            'borderColor': color,
            'extendedProps': {
                'subject': str(booking.subject),
                'email': booking.email,
                'phone': booking.phone_number,
                'time': str(booking.preferred_time),
                'claimed_by': booking.claimed_by.username if booking.claimed_by else None,
                'is_past': is_past,
            }
        })
    

    return JsonResponse(events, safe=False)

def public_teacher_profile(request, slug):
    teacher = get_object_or_404(TeacherProfile, slug=slug)
    return render(request, 'users/teacher_profile.html', {'teacher': teacher})

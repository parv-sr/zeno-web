from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bookings.models import Booking

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
    bookings = Booking.objects.all().order_by('-timestamp')
    return render(request, "users/dashboard.html", {'bookings' : bookings})
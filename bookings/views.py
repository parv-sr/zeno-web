from django.shortcuts import render
from .forms import BookingForm
from django.core.mail import send_mail
from django.conf import settings

def book_class(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            user_email = form.cleaned_data['email']


            subject = 'New Class booking'
            message = f"""
            Name: {booking.full_name}
            Email: {booking.email}
            Phone: {booking.phone_number}
            Subject: {booking.subject}
            Date: {booking.preferred_date}
            Time: {booking.preferred_time}
            """.strip()
            
            send_mail(                                     
                subject,
                message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
            )

            return render(request, 'bookings/success.html')
    else:
        form = BookingForm()
    
    return render(request, 'bookings/booking_form.html', {'form': form})

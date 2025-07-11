from django.shortcuts import render
from .forms import BookingForm, FeedbackForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def book_class(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            user_email = form.cleaned_data['email']

            subject = 'Your Zeno Class is Confirmed!'
            text_content = "Thank you for booking with Zeno Learning. Please enable HTML to view this email properly."

            html_content = render_to_string('emails/booking_confirmation.html', {
                'full_name': booking.full_name,
                'email': booking.email,
                'phone': booking.phone_number,
                'subject': booking.subject,
                'date': booking.preferred_date,
                'time': booking.preferred_time,
            })

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[user_email],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return render(request, 'bookings/success.html')
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'bookings/feedback_success.html')
    else:
        form = FeedbackForm()
    return render(request, 'bookings/feedback.html', {'form': form})
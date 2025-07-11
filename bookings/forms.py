from django import forms
from .models import Booking, Feedback
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone_number', 'subject', 'preferred_date', 'preferred_time']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control bg-light-subtle text-dark'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light-subtle text-dark'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control bg-light-subtle text-dark'}),
            'subject': forms.Select(attrs={'class': 'form-control bg-light-subtle text-dark'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bg-light-subtle text-dark'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control bg-light-subtle text-dark'}),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not phone.isdigit() or len(phone) != 10:
            raise forms.ValidationError("Enter a 10 digit phone number.")
        return phone
    
    def clean_preferred_date(self):
        preferred_date = self.cleaned_data.get('preferred_date')
        if preferred_date < date.today():
            raise forms.ValidationError("You cannot select a past date.")
        return preferred_date
    
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows':4})
        }
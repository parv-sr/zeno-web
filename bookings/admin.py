from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'preferred_date', 'preferred_time', 'timestamp')
    search_fields = ('full_name', 'email', 'subject')
    list_filter = ('subject', 'preferred_date')

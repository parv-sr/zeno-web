from django.contrib import admin
from .models import Booking, Subject


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'subject',
        'preferred_date',
        'preferred_time',
        'timestamp',
        'claimed_by',
    )
    search_fields = ('full_name', 'email', 'subject__name', 'claimed_by__username')
    list_filter = ('subject', 'preferred_date', 'claimed_by')
    list_select_related = ('subject', 'claimed_by')  # Optimization


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

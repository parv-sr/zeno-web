from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    claimed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='claimed_bookings')

    def __str__(self):
        return f"{self.full_name} - {self.subject} on {self.preferred_date}"




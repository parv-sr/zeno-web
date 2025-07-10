from django.db import models


class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject} on {self.preferred_date}"



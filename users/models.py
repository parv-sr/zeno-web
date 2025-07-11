from django.db import models
from django.contrib.auth.models import User
from bookings.models import Subject

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.user.username} - {'Teacher' if self.is_teacher else 'Not a Teacher'}"


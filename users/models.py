from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from bookings.models import Subject

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject)
    
    # New fields for the public profile
    bio = models.TextField(blank=True)
    education = models.CharField(max_length=255, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.user.username}-{self.id}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {'Teacher' if self.is_teacher else 'Not a Teacher'}"

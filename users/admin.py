from django.contrib import admin
from .models import TeacherProfile
from django.utils.text import slugify

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_teacher', 'linkedin_url')

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.user.username)
        super().save_model(request, obj, form, change)

# Safe registration
try:
    admin.site.register(TeacherProfile, TeacherProfileAdmin)
except admin.sites.AlreadyRegistered:
    pass

# populate_slugs.py

import os
import django

# Setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zeno_web.settings")
django.setup()

from users.models import TeacherProfile
from django.utils.text import slugify

for profile in TeacherProfile.objects.all():
    if not profile.slug:
        profile.slug = slugify(f"{profile.user.username}-{profile.id}")
        profile.save()
        print(f"Slug set for {profile.user.username} -> {profile.slug}")

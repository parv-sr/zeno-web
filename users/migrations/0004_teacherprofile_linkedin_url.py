# Generated by Django 5.2.4 on 2025-07-18 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_teacherprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherprofile',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

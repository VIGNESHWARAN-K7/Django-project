# Generated by Django 5.1 on 2024-08-18 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]

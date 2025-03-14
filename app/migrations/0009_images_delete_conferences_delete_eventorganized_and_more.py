# Generated by Django 5.1 on 2024-08-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Conferences',
        ),
        migrations.DeleteModel(
            name='Eventorganized',
        ),
        migrations.DeleteModel(
            name='FoundedProject',
        ),
        migrations.DeleteModel(
            name='InvitedTalks',
        ),
        migrations.DeleteModel(
            name='Paper',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.DeleteModel(
            name='Seminars',
        ),
        migrations.DeleteModel(
            name='Subject_experience',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]

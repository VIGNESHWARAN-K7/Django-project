# Generated by Django 5.1 on 2024-08-18 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_images_delete_conferences_delete_eventorganized_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField(blank=True, max_length=50)),
                ('content', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='heading',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-27 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_me_app', '0003_info_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='progress_bar',
        ),
        migrations.RemoveField(
            model_name='info',
            name='skills',
        ),
    ]

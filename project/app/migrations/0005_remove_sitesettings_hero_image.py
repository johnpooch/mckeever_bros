# Generated by Django 4.0.1 on 2022-01-25 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_sitesettings_courses_manual_handling_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesettings',
            name='hero_image',
        ),
    ]
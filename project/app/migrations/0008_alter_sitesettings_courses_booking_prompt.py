# Generated by Django 4.0.1 on 2022-04-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_sitesettings_courses_booking_prompt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='courses_booking_prompt',
            field=models.TextField(default=''),
        ),
    ]
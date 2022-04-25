# Generated by Django 4.0.1 on 2022-04-25 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_add_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='nav_online_courses',
            field=models.CharField(default='Online Courses', help_text='Text for nav item which brings the user to the online courses section.', max_length=20),
        ),
    ]
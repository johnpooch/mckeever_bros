# Generated by Django 4.0.1 on 2022-01-21 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sitesettings_hero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='courses_manual_handling_description',
            field=models.TextField(blank=True, help_text='Paragraph under manual handing header in courses section', null=True),
        ),
    ]
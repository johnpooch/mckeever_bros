from django.db import migrations
from django.db import transaction


def create_data(apps, schema_editor):
    SiteSettings = apps.get_model('app', 'SiteSettings')
    site_settings = SiteSettings.objects.get()
    site_settings.courses_booking_prompt = "To book a course, <a href=\"#contact\">get in touch</a> or <a href=\"https://mckeeverbrossafety.mykademy.com/\" target=\"_blank\">create a booking online</a>."
    site_settings.nav_courses = "Courses"
    site_settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_add_data'),
    ]

    operations = [
        migrations.RunPython(
            create_data,
            reverse_code=migrations.RunPython.noop
        ),
    ]


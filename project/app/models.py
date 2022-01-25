from django.db import models

class SiteSettings(models.Model):

    title = models.CharField(max_length=200, help_text="The title of the site. Appears at the top of the browser in the tab and also appears in the copyright at the bottom")

    # Nav items
    nav_courses = models.CharField(max_length=20, help_text="Text for nav item which brings the user to the courses section.")
    nav_contact = models.CharField(max_length=20, help_text="Text for nav item which brings the user to the contact section.")

    # Hero
    hero_header = models.CharField(max_length=200, help_text="Big header that appears on the hero section.")
    hero_description = models.TextField(help_text="Paragraph that appears under the hero header.")
    hero_button_label = models.CharField(max_length=50, help_text="Text that appears inside the button on the hero page.")

    # About
    about_column_one_header = models.CharField(max_length=200, help_text="Header for first column in about section")
    about_column_one_description = models.TextField(help_text="Paragraph for first column in about section")

    about_column_two_header = models.CharField(max_length=200, help_text="Header for second column in about section")
    about_column_two_description = models.TextField(help_text="Paragraph for second column in about section")

    about_column_three_header = models.CharField(max_length=200, help_text="Header for third column in about section")
    about_column_three_description = models.TextField(help_text="Paragraph for third column in about section")

    # Courses
    courses_header = models.CharField(max_length=200, help_text="Header for courses section")
    courses_description = models.TextField(help_text="Paragraph that appears under header in courses section")

    courses_manual_handling_header = models.CharField(max_length=200, help_text="Header for manual handing sub-section in courses section")
    courses_manual_handling_description = models.TextField(help_text="Paragraph under manual handing header in courses section", blank=True, null=True)

    courses_other_courses_header = models.CharField(max_length=200, help_text="Header for other courses sub-section in courses section")
    courses_other_courses_description = models.TextField(help_text="Paragraph under other courses header in courses section")

    # Reviews
    reviews_header = models.CharField(max_length=200, help_text="Header that appears on the reviews section.")
    reviews_column_one_description = models.TextField(help_text="Paragraph for first column in reviews section")
    reviews_column_one_author = models.CharField(max_length=200, help_text="Author for first column in reviews section")

    reviews_column_two_description = models.TextField(help_text="Paragraph for second column in reviews section")
    reviews_column_two_author = models.CharField(max_length=200, help_text="Author for second column in reviews section")

    reviews_column_three_description = models.TextField(help_text="Paragraph for third column in reviews section")
    reviews_column_three_author = models.CharField(max_length=200, help_text="Author for third column in reviews section")

    # Contact
    contact_header = models.CharField(max_length=200, help_text="Header that appears on the contact section.")
    contact_description = models.TextField(help_text="Paragraph that appears under the contact header.")
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Socials
    linkedin = models.URLField(max_length=128, blank=True)
    instagram = models.URLField(max_length=128, blank=True)


class ManualHandlingSummaryItem(models.Model):
    label = models.CharField(max_length=100, help_text="The text that appears for the item.")
    icon_name = models.CharField(max_length=100, help_text="The code for the Font Awesome icon. See https://fontawesome.com/v5/cheatsheet. Example: address-book")


class ManualHandlingCourseOutlineItem(models.Model):
    label = models.CharField(max_length=100, help_text="The text that appears for the item.")


class OtherCoursesItem(models.Model):
    label = models.CharField(max_length=100, help_text="The text that appears for the item.")
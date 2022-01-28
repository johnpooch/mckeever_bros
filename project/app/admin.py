from django.contrib import admin
from .models import ManualHandlingSummaryItem, ManualHandlingCourseOutlineItem, OtherCoursesItem, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(ManualHandlingCourseOutlineItem)
class ManualHandlingCourseOutlineItemAdmin(admin.ModelAdmin):
    pass


@admin.register(ManualHandlingSummaryItem)
class ManualHandlingSummaryItemAdmin(admin.ModelAdmin):
    pass


@admin.register(OtherCoursesItem)
class OtherCoursesItemAdmin(admin.ModelAdmin):
    pass
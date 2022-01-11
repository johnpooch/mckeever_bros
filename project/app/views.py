from app import models
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_settings"] = models.SiteSettings.objects.get()
        context["manual_handling_summary_items"] = models.ManualHandlingSummaryItem.objects.all()
        context["manual_handling_course_outline_items"] = models.ManualHandlingCourseOutlineItem.objects.all()
        context["other_courses_items"] = models.OtherCoursesItem.objects.all()
        return context
    


class StyleView(TemplateView):
    template_name = "style.html"
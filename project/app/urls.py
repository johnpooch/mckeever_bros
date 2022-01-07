from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('style', views.StyleView.as_view(), name='style'),
]
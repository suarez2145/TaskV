from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'employee'
urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('employer', TemplateView.as_view(template_name="employer_home.html"), name='employer'),
    path('checklist', TemplateView.as_view(template_name="checklist.html"), name='checklist')
]


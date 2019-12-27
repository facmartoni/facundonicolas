"""Posts views"""

# Django

from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'

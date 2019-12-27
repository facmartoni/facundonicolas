"""Posts views"""

# Django

from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'base.html'


class PostView(TemplateView):
    template_name = 'base.html'


class TagView(TemplateView):
    template_name = 'base.html'

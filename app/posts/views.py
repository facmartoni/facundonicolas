"""Posts views"""

# Python

import random

# Django

from django.views.generic import ListView, TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_number = random.randint(1, 4)
        context["random_number"] = str(random_number)
        return context


class PostView(TemplateView):
    template_name = 'base.html'


class TagView(TemplateView):
    template_name = 'base.html'

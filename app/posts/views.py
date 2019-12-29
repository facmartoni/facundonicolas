"""Posts views"""

# Python

import random
from datetime import datetime

# Django

from django.views.generic import ListView, TemplateView

# Own

from posts.forms import SubscriberForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Random number for random bitmoji
        random_number = random.randint(1, 4)
        context["random_number"] = str(random_number)

        # Subscriber form
        form = SubscriberForm()
        context["form"] = form

        # Actual year
        year = datetime.now().year
        context["year"] = year

        return context


class PostView(TemplateView):
    template_name = 'base.html'


class TagView(TemplateView):
    template_name = 'base.html'

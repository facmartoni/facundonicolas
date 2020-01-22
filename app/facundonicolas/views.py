"""Main views"""

# Python

import random
from datetime import datetime

# Django

from django.views.generic import TemplateView
from django.shortcuts import render, redirect

# Own

from posts.forms import SubscriberForm


def wip(request):
    context = {}

    # Actual year
    year = datetime.now().year
    context["year"] = year

    # Subscriber form
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:confirmation')
    else:
        form = SubscriberForm()
    context["form"] = form

    return render(request, 'wip.html', context)


def not_found(request):
    context = {}

    # Random number for random bitmoji
    random_number = random.randint(1, 3)
    context["random_number"] = str(random_number)

    # Actual year
    year = datetime.now().year
    context["year"] = year

    # Subscriber form
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:confirmation')
    else:
        form = SubscriberForm()
    context["form"] = form

    return render(request, '404.html', context)

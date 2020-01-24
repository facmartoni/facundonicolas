"""Posts views"""

# Python

import random
from datetime import datetime

# Django

from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect

# Third Party

from ipware import get_client_ip

# Own

from posts.forms import SubscriberForm
from posts.models import Subscriber, Post

"""The number of registers allowed per IP"""
NUMBER_OF_IPS_ALLOWED = 20


def home_view(request):

    context = {}

    # Random number for random bitmoji
    random_number = random.randint(1, 4)
    context["random_number"] = str(random_number)

    # Actual year
    year = datetime.now().year
    context["year"] = year

    # Subscriber form
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():

            # Add ipv4 to form
            """If an ip registers an user more than NUMBER_OF_IPS_ALLOWED times, 
               the program doesn't save the subscriber in the DB"""
            ip, is_routable = get_client_ip(request)
            if ip:
                qty_ips = len(Subscriber.objects.filter(ipv4=ip))
                if qty_ips <= NUMBER_OF_IPS_ALLOWED:
                    form.instance.ipv4 = ip
                    form.save()

            return redirect('posts:confirmation')
    else:
        form = SubscriberForm()
    context["form"] = form

    # Posts

    posts = Post.objects.all().order_by('-pub_date')
    context["posts"] = posts

    return render(request, 'views/home.html', context)


def confirmation_view(request):
    context = {}

    # Actual year
    year = datetime.now().year
    context["year"] = year

    # Subscriber form
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():

            # Add ipv4 to form
            """If an ip registers an user more than NUMBER_OF_IPS_ALLOWED times, 
               the program doesn't save the subscriber in the DB"""
            ip, is_routable = get_client_ip(request)
            if ip:
                qty_ips = len(Subscriber.objects.filter(ipv4=ip))
                if qty_ips <= NUMBER_OF_IPS_ALLOWED:
                    form.instance.ipv4 = ip
                    form.save()

            return redirect('posts:confirmation')
    else:
        form = SubscriberForm()
    context["form"] = form

    return render(request, 'views/confirmation.html', context)


def post_detail(request, slug):
    pass


def tag_detail(request, slug):
    pass

# Python

import re

# Django

from django import forms

# Own

from posts.models import Subscriber


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('name', 'email')

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.capitalize()

    def clean_email(self):
        email = self.cleaned_data['email']
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not (re.match(email_regex, email)):
            raise forms.ValidationError("Ingresa un email válido :(")
        return email

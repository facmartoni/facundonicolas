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

        # # Valid email
        # email_regex = re.compile(
        #     r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        # if not (re.match(email_regex, email)):
        #     raise forms.ValidationError("Ingresa un email válido")

        # Email does not exist
        email_taken = Subscriber.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError("Este email ya está suscrito")

        return email

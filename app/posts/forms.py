# Django

from django import forms

# Own

from posts.models import Subscriber


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = ('name', 'email')

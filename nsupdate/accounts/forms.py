# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth import get_user_model


class UserProfileForm(forms.ModelForm):
    class Meta(object):
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'email': forms.widgets.TextInput(attrs=dict(autofocus=None)),
        }

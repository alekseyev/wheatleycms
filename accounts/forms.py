from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class AccountCreationForm(UserCreationForm):
    email = forms.EmailField(label = _('E-mail'))
    
    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'username', 'email', 'password1', 'password2', 
        ]

    def save(self, commit=True):
        user = super(AccountCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return user

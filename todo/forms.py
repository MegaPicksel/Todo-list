from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Registration form
class RegistrationForm(UserCreationForm):
    email= forms.EmailField(required=True, label='email')
    first_name = forms.CharField(required=True)

    # Set the help texts for password fields in form to none
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)







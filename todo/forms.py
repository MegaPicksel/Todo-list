from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    username = forms.EmailField(required=True, label='email')
    first_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            subject = 'account confirmation'
            message = 'Please click the link to complete registartion. http://127.0.0.1:8000/todo/login/'
            from_email = 'django.testacc306@gmail.com'
            to = [user.username]
            send_mail(subject, message, from_email, to, fail_silently=False)

        return user


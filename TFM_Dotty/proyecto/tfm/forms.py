from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')
    location = forms.CharField(max_length=30, help_text='Location')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'location')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='Subject', required=True)
    comment = forms.CharField(max_length=500, help_text='Comment', required=True)

    class Meta:
        fields = ('subject', 'comment')

class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
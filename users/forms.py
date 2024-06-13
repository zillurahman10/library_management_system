from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Account

class RegistrationForm(UserCreationForm):
    # # profile_image = forms.FileField()
    username = forms.CharField( widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input input-bordered'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input input-bordered'}))
    shipping_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input-bordered'}))

    class Meta:
        model = User
        fields = '__all__'
        
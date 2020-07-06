from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from profiles.models import Profile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Julius'}))
    last_name = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Caesar'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'jCaesar@gmail.com'}))

    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password1","password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','field_of_interest','image']
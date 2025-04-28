from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomSignUpForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        label="Full Name",
        widget=forms.TextInput(attrs={'id': 'full-name'})
    )
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={'id': 'email'})
    )
    company = forms.CharField(
        max_length=100,
        required=False,
        label="Company Name",
        widget=forms.TextInput(attrs={'id': 'company'})
    )
    terms = forms.BooleanField(
        required=True,
        label="I agree to the Terms of Service and Privacy Policy",
        widget=forms.CheckboxInput(attrs={'id': 'terms'})
    )

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'company', 'password1', 'password2', 'terms']
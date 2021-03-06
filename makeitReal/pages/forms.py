from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Surname'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']

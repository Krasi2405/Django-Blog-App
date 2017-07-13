from django import forms
from django.core import validators


class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)
	honeypot = forms.CharField(widget=forms.HiddenInput, required=False,
		validators=[validators.MaxLengthValidator(0)])
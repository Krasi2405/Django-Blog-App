from django import forms

class SearchForm(forms.Form):
	search_field = forms.CharField(max_length = 255, required=False)
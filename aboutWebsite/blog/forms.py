from django import forms

from . import category_choices
class SearchForm(forms.Form):
	search_field = forms.CharField(max_length = 255, required=False)
	categories = forms.ChoiceField(choices = category_choices.CHOICES)
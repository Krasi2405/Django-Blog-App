from django import forms

from . import category_choices
from . import models
class SearchForm(forms.Form):
	search_field = forms.CharField(max_length = 255, required=False)
	categories = forms.ChoiceField(choices = category_choices.CHOICES)

'''
class ImageForm(forms.ModelForm):
	class Meta:
		model = models.Image
		exclude = ()

ImageFormSet = inlineformset_factory(models.Blog, models.Image, 
									 form = ImageForm, extra = 1)	
'''


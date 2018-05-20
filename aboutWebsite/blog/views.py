from django.shortcuts import render, get_object_or_404

import itertools

from .models import Blog, Paragraph, Image, Category
from . import forms

# Create your views here.
def blog_list(request):
	blogs = Blog.objects.all()
	search_form = forms.SearchForm()
	if request.method == "GET":
		search_form = forms.SearchForm(request.GET)
		if search_form.is_valid():
			category_name = search_form.cleaned_data['categories']
			if(category_name != "all"):
				for category in Category.objects.all():
					if category_name == category.name:
						chosen_category = category
						break
				blogs = chosen_category.blog_set.all()

			regex = r'\b{}\b'.format(search_form.cleaned_data['search_field'])
			blogs = blogs.filter(title__regex=regex)
			
	return render(request, 'blog/blog_list.html', 
		{'blog_list': blogs, 'search_form': search_form})


def blog_detail(request, pk):
	blog = Blog.objects.get(pk=pk)
	images = blog.image_set.all()
	paragraphs = blog.paragraph_set.all()
	blog_parts_list = list(images) + list(paragraphs)
	blog_parts_list.sort(key=lambda x: x.order)
	return render(request, 'blog/blog_detail.html', 
		{'blog': blog, 'blog_parts_list': blog_parts_list})

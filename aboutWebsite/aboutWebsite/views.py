from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.contrib import messages

from blog.models import Blog
from . import forms
def index(request):
	blog = Blog.objects.filter(shareable=True).order_by("-id")
	blog = get_object_or_404(blog)
	images = blog.image_set.all()
	paragraphs = blog.paragraph_set.all()
	blog_parts_list = list(images) + list(paragraphs)
	blog_parts_list.sort(key=lambda x: x.order)
	return render(request, 'blog/blog_detail.html', 
		{'blog': blog, 'blog_parts_list': blog_parts_list})


def about(request):
	return render(request, 'about.html')


def contact(request):
	form = forms.ContactForm()
	if request.method == "POST":
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			send_mail(
				"Server contact message from {name} by <{email}>".format(**form.cleaned_data),
				form.cleaned_data['content'],
				form.cleaned_data['email'],
				["krasi2405@gmail.com"]
			)
			messages.add_message(request, messages.SUCCESS, "Email sent!")
			return HttpResponseRedirect(reverse('contact'))

	return render(request, 'contact.html', {'form': form})

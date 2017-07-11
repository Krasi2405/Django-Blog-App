from django.shortcuts import render, get_object_or_404

from blog.models import Blog
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
	return render(request, 'contact.html')

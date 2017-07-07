from django.shortcuts import render, get_object_or_404

from .models import Blog, Paragraph, Image

# Create your views here.
def blog_list(request):
	blogs = Blog.objects.all()
	return render(request, 'blog_list.html', {'blog_list': blogs})


def blog_detail(request, pk):
	blog = Blog.objects.get(pk=pk)
	images = Image.objects.all()
	paragraphs = Paragraph.objects.all()
	blog_parts_list = list(images) + list(paragraphs)
	blog_parts_list.sort(key=lambda x: x.order)
	return render(request, 'blog_detail.html', 
		{'blog': blog, 'blog_parts_list': blog_parts_list})
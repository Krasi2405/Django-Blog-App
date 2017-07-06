from django.contrib import admin

from .models import Blog, Image, Paragraph

class ImageInLine(admin.StackedInline):
	model = Image

class ParagraphInLine(admin.StackedInline):
	model = Paragraph

class BlogAdmin(admin.ModelAdmin):
	inlines = [ImageInLine, ParagraphInLine, ]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Image)
admin.site.register(Paragraph)

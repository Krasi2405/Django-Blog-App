from django.contrib import admin

from . import models

class ImageInLine(admin.StackedInline):
	model = models.Image

class ParagraphInLine(admin.StackedInline):
	model = models.Paragraph

	
class BlogAdmin(admin.ModelAdmin):
	inlines = [ImageInLine, ParagraphInLine]

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Image)
admin.site.register(models.Paragraph)
admin.site.register(models.Category)

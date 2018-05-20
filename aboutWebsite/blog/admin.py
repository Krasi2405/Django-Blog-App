from django.contrib import admin

from . import models

class ImageInLine(admin.TabularInline):
	model = models.Image

class ParagraphInLine(admin.StackedInline):
	model = models.Paragraph

	
class BlogAdmin(admin.ModelAdmin):
	inlines = [ImageInLine, ParagraphInLine]
	fieldsets = (
		(None, {"fields": ("title", "writer", "categories", "shareable")}),
	)
	search_fields = ["title", "writer"]
	list_filter = ["categories"]
	list_display = ["title", "writer", "shareable", "blog_categories"]
	list_editable = ["writer", "shareable"]
	

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category)

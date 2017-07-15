from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	writer = models.CharField(max_length = 255)
	shareable = models.BooleanField(default = False)
	categories = models.ManyToManyField("Category")

	class Meta():
		ordering = ['-created_at', ]

	def __str__(self):
		return self.title


class Image(models.Model):
	src = models.ImageField(upload_to = "assets/images")
	blog = models.ForeignKey(Blog)
	order = models.IntegerField(default = 0)

	def path(self):
		image_path = self.src.url.split('/')[1:]
		return '/'.join(image_path)

	def __str__(self):
		return self.path()

class Paragraph(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog)
	order = models.IntegerField(default = 0)

	def __str__(self):
		return self.text


class Category(models.Model):
	name = models.CharField(max_length = 255)

	def __str__(self):
		return self.name
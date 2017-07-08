from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	writer = models.CharField(max_length = 255)

	class Meta():
		ordering = ['-created_at', ]


class Image(models.Model):
	src = models.ImageField(upload_to = "assets/images")
	blog = models.ForeignKey(Blog)
	order = models.IntegerField(default = 0)

	def path(self):
		image_path = self.src.url.split('/')[1:]
		return '/'.join(image_path)


class Paragraph(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog)
	order = models.IntegerField(default = 0)



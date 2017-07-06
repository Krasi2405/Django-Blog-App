from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	writer = models.CharField(max_length = 255)

# Dont use just yet cant figure out how to upload images!
class Image(models.Model):
	src = models.ImageField()
	blog = models.ForeignKey(Blog)
	order = models.IntegerField(default = 0)


class Paragraph(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog)
	order = models.IntegerField(default = 0)



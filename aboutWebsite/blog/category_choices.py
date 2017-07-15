from .models import Category

CHOICES = [("all", "All")]
index = 1
for category in Category.objects.all():
	CHOICES.append(("{}".format(category.name), "{}".format(category.name)))
	index += 1


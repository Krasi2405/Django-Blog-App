from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 255)
	game_files = models.FileField(upload_to="assets/games")
	shareable = models.BooleanField(default = False)
	release_date = models.DateTimeField(auto_now_add = True)
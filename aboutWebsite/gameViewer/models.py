from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import os
import patoolib


def get_upload_path(instance, filename):
	base_game_path = os.path.join("assets", "games")
	return os.path.join(base_game_path, filename)


# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 255)
	game_files = models.FileField(upload_to=get_upload_path)
	shareable = models.BooleanField(default = False)
	release_date = models.DateTimeField(auto_now_add = True)

	def get_extracted_dir_path(self):
		base_game_path = os.path.join(os.path.join("assets", "games"))
		extracted_dir = os.path.join(base_game_path, self.name)
		return extracted_dir

	def get_startup_file_path(self):
		return os.path.abspath(os.path.join(self.get_extracted_dir_path(), "index.html"))


@receiver(post_save, sender = Game)
def unpack_game(sender, instance, **kwargs):
	out_dir = instance.get_extracted_dir_path()
	os.makedirs(os.path.abspath(out_dir))

	patoolib.extract_archive(
		instance.game_files.name,
		outdir = out_dir)

	os.remove(os.path.abspath(instance.game_files.name))
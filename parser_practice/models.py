from django.db import models

class Kaktus_media_parser(models.Model):
	img = models.ImageField(upload_to = '')
	title = models.CharField(max_length = 500, null = True)
	time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self): return self.title
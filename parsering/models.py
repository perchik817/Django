from django.db import models

class Tv_parser(models.Model):
	title = models.CharField(max_length = 100)
	title_text = models.CharField(max_length = 200, null = True)
	img = models.ImageField(upload_to = '')
	
	def __str__(self):
		return self.title
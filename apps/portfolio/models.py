from django.db import models

class Portfolio(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	image = models.ImageField(upload_to = 'portfolio/$Y/M')

	def __str__(self):
		return self.title
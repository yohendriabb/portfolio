from django.db import models

class Category(models.Model):
	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'

	parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=250, unique=True)

	def __str__(self):
		return self.name

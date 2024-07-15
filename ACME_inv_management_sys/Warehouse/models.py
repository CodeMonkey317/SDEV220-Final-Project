from django.db import models
from django.contrib.auth.models import User


class InventoryItem(models.Model):
	name = models.CharField(max_length=200)
	stock = models.IntegerField()
	type = models.ForeignKey('Type', on_delete=models.SET_NULL, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
	
class Type(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'type'

	def __str__(self):
		return self.name

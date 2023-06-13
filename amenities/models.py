from django.db import models

# Create your models here.


class Amenities(models.Model):
	productname=models.CharField(max_length=20)
	price=models.IntegerField()
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.productname

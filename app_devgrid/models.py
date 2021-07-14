from django.db import models

# Create your models here.

class Table_Id_City(models.Model):
	country_id = models.CharField(max_length=30, null=True, blank=True)
	country = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=10, null=True, blank=True)
	lon = models.CharField(max_length=80, null=True, blank=True)
	lat = models.CharField(max_length=80, null=True, blank=True)

	
	def __str__(self):
		return 'ID City: {} --- Name City: {}'.format(self.country_id, self.country)



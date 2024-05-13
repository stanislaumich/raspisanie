from django.db import models

class Aud(models.Model):
	#fio = models.CharField(max_length=100)
	#fam = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	descr = models.CharField(max_length=200)
	#idpers = models.IntegerField()
	#dolg = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
    # Methods
	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])
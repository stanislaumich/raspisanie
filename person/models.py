from django.db import models

class Person(models.Model):
	fio = models.CharField(max_length=100)
	fam = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	otch = models.CharField(max_length=100)
	born = models.IntegerField()
	dolg = models.CharField(max_length=100)
	def __str__(self):
		return self.fio
	class Meta:
		ordering = ['fio']
    # Methods
	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])

class Rasp(models.Model):
	#fio = models.CharField(max_length=100)
	#fam = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	#otch = models.CharField(max_length=100)
	idpers = models.IntegerField()
	#dolg = models.CharField(max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
    # Methods
	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])


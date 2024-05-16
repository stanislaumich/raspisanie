from django.db import models
#from .models import Person, Para, Aud, Predmet, Grp

import datetime
#https://www.geeksforgeeks.org/datefield-django-models/?ref=lbp
# creating an instance of
# datetime.date
#d = datetime.date(1997, 10, 19)
class Rasp(models.Model):
	#dt = models.DateField("Дата")
	#dw = models.IntegerField("День недели", default = 0)
	name = models.CharField("Название", max_length=100)
	#idgrp = models.ForeignKey(Grp, on_delete=models.CASCADE)
	#idpers = models.ForeignKey(Person, on_delete=models.CASCADE)
	#idpara = models.ForeignKey(Para, on_delete=models.CASCADE)
	#idaud = models.ForeignKey(Aud, on_delete=models.CASCADE)
	#idpredmet = models.ForeignKey(Predmet, on_delete=models.CASCADE)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
    # Methods
	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])
	class Meta:
		verbose_name = "Расписание"
		verbose_name_plural = "Расписания"


class Para(models.Model):
    name = models.CharField("Название", max_length=100)
    num = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    class Meta:
        verbose_name = "Пара"
        verbose_name_plural = "Пары"



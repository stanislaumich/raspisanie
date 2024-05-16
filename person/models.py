from django.db import models

class Person(models.Model):
	fio = models.CharField("ФИО",max_length=100)
	fam = models.CharField("Фамилия",max_length=100)
	name = models.CharField("Имя",max_length=100)
	otch = models.CharField("Отчество",max_length=100)
	born = models.IntegerField("Год. рожд.")
	dolg = models.CharField("Должность",max_length=100)
	def __str__(self):
		return self.fio
	class Meta:
		ordering = ['fio']
    # Methods
	def get_absolute_url(self):
		return reverse('model-detail-view', args=[str(self.id)])
	class Meta:
		verbose_name = "Преподаватель"
		verbose_name_plural = "Преподаватели"
		
		

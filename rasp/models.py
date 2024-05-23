from django.db import models
#from .models import Person, Para, Aud, Predmet, Grp

class Para(models.Model):
	name = models.CharField("Название", max_length=100)
	num = models.IntegerField(default=0)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['num']
		verbose_name = "Пара"
		verbose_name_plural = "Пары"
	#def get_absolute_url(self):
	#	return reverse('model-detail-view', args=[str(self.id)])

class Aud(models.Model):
	name = models.CharField("Название",max_length=100)
	descr = models.CharField("Описание",max_length=200)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
		verbose_name = "Аудитория"
		verbose_name_plural = "Аудитории"

class Grp(models.Model):
	num = models.CharField("Номер", max_length=30)
	name = models.CharField("Название", max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']
		verbose_name = "Группа"
		verbose_name_plural = "Группы"
	#def get_absolute_url(self):
	#	return reverse('model-detail-view', args=[str(self.id)])

class Person(models.Model):
	fio = models.CharField("ФИО", max_length=100)
	fam = models.CharField("Фамилия", max_length=100)
	name = models.CharField("Имя", max_length=100)
	otch = models.CharField("Отчество", max_length=100)
	born = models.IntegerField("Год. рожд.")
	dolg = models.CharField("Должность", max_length=100)
	def __str__(self):
		return self.fio
	class Meta:
		ordering = ['fio']
		verbose_name = "Преподаватель"
		verbose_name_plural = "Преподаватели"

class Predmet(models.Model):
	name = models.CharField("Название",max_length=100)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['id']
		verbose_name = "Предмет"
		verbose_name_plural = "Предметы"

class Rasp(models.Model):
	dt = models.DateField("Дата", null=True)
	name = models.CharField("Название", max_length=100)
	idgrp = models.ForeignKey(Grp, verbose_name="Группа",on_delete=models.PROTECT, default = 0)
	idpers = models.ForeignKey(Person,verbose_name="Преподаватель", on_delete=models.PROTECT, default = 0)
	idpara = models.ForeignKey(Para, verbose_name="Пара",on_delete=models.PROTECT, default = 0)
	idaud = models.ForeignKey(Aud,verbose_name="Аудитория", on_delete=models.PROTECT, default = 0)
	idpredmet = models.ForeignKey(Predmet,verbose_name="Предмет", on_delete=models.PROTECT, default = 0)
	def __str__(self):
		return self.idpara.name
	class Meta:
		ordering = ['id']
		#unique_together = ('idgrp', 'idpers', 'idpara','idaud', 'idpredmet','dt')
		verbose_name = "Расписание"
		verbose_name_plural = "Расписания"




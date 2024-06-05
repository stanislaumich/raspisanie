from django.db import models

from person.models import Person


# from rasp.models import Person


class Aud(models.Model):
    name = models.CharField("Название", max_length=100)
    descr = models.CharField("Описание", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"


class MyAud(models.Model):
    myid = models.ForeignKey(Person, related_name='audme', verbose_name="Хозяин", on_delete=models.PROTECT,
                             default=0)
    audid = models.ForeignKey(Aud, related_name='audany', verbose_name="Аудитория", on_delete=models.PROTECT,
                               default=0)

    def __str__(self):
        return self.myid.fio

    class Meta:
        ordering = ['id']
        unique_together = ('myid', 'audid')
        verbose_name = "Список аудиторий"
        verbose_name_plural = "Списки аудиторий"

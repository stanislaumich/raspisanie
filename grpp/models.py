# python manage.py migrate --fake-initial
from django.db import models

from person.models import Person


# from rasp.models import Person

class Grp(models.Model):
    num = models.CharField("Номер", max_length=30)
    name = models.CharField("Название", max_length=100)
    kurs = models.IntegerField("Курс",blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

class MyGrp(models.Model):
    myid = models.ForeignKey(Person, related_name='grpme', verbose_name="Хозяин", on_delete=models.PROTECT,
                             default=0)
    grpid = models.ForeignKey(Grp, related_name='grpany', verbose_name="Группа", on_delete=models.PROTECT,
                               default=0)

    def __str__(self):
        return self.myid.fio + ' - ' + self.grpid.name

    class Meta:
        ordering = ['id']
        unique_together = ('myid', 'grpid')
        verbose_name = "Список групп"
        verbose_name_plural = "Списки групп"

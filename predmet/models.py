from django.db import models
from person.models import Person


class Predmet(models.Model):
    name = models.CharField("Название", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

class MyPredmet(models.Model):
    myid = models.ForeignKey(Person, related_name='predmetme', verbose_name="Хозяин", on_delete=models.PROTECT,
                             default=0)
    predmetid = models.ForeignKey(Predmet, related_name='predmetany', verbose_name="Предмет", on_delete=models.PROTECT,
                               default=0)

    def __str__(self):
        return self.myid.fio + '' + self.predmetid.name

    class Meta:
        ordering = ['id']
        unique_together = ('myid', 'predmetid')
        verbose_name = "Список предметов"
        verbose_name_plural = "Списки предметов"


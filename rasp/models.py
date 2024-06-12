from datetime import datetime

from django.db import models

from aud.models import Aud, MyAud
from grpp.models import Grp
from para.models import Para
from person.models import Person, MyPers
from predmet.models import Predmet


class Rasp(models.Model):
    dt = models.DateField("Дата", null=True)
    name = models.CharField("Название", max_length=100, null=True, blank=True)
    idgrp = models.ForeignKey(Grp, verbose_name="Группа", on_delete=models.PROTECT, default=0)
    idpers = models.ForeignKey(Person, verbose_name="Преподаватель", on_delete=models.PROTECT, default=0)
    idpara = models.ForeignKey(Para, verbose_name="Пара", on_delete=models.PROTECT, default=0)
    idaud = models.ForeignKey(Aud, verbose_name="Аудитория", on_delete=models.PROTECT, default=0)
    idpredmet = models.ForeignKey(Predmet, verbose_name="Предмет", on_delete=models.PROTECT, default=0)

    def __str__(self):
        return self.idpara.name

    class Meta:
        ordering = ['id']
        # unique_together = ('idgrp', 'idpers', 'idpara','idaud', 'idpredmet','dt')
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
        # unique_together = ('dt', 'idpara', 'idgrp')
        # unique_together = ('dt', 'idpara', 'idaud')
        # unique_together = ('dt', 'idpara', 'idpers')
        constraints = [
            models.UniqueConstraint(fields=['dt', 'idpara', 'idgrp'], name='cidgrp'),
            models.UniqueConstraint(fields=['dt', 'idpara', 'idaud'], name='cidaud'),
            models.UniqueConstraint(fields=['dt', 'idpara', 'idpers'], name='cidpers')
        ]


class Reserv(models.Model):
    dt = models.DateField("Дата", null=True)
    name = models.CharField("Название", max_length=100, null=True, blank=True)
    idpers = models.ForeignKey(Person, related_name='iddest', verbose_name="Преподаватель", on_delete=models.PROTECT,
                               default=0)
    idpara = models.ForeignKey(Para, verbose_name="Пара", on_delete=models.PROTECT, default=0)
    idmaster = models.ForeignKey(Person, related_name='idmaster', verbose_name="Хозяин", on_delete=models.PROTECT,
                                 default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = "Резерв"
        verbose_name_plural = "Резерв"


class XlsRaspPers(models.Model):
    idpers = models.ForeignKey(Person, related_name='idxlsrasppers', verbose_name="Преподаватель",
                               on_delete=models.PROTECT,
                               default=0)
    idpara = models.ForeignKey(Para, verbose_name="Пара", on_delete=models.PROTECT, default=0)
    nk = models.IntegerField("Номер колонки", null=True, blank=True)
    nd = models.IntegerField("Номер дня", null=True, blank=True)
    # np = models.IntegerField("Номер занятия", null=True, blank=True)
    xls = models.CharField("Ячейка А1", max_length=10, null=True, blank=True)
    dop1 = models.CharField("Доп1", max_length=200, null=True, blank=True)
    dop2 = models.CharField("Доп2", max_length=200, null=True, blank=True)
    xlsrow = models.IntegerField("Строка", null=True, blank=True)
    xlscol = models.IntegerField("Столбец", null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Бланк"
        verbose_name_plural = "Бланки"

from django.db import models


class Person(models.Model):
    fio = models.CharField("ФИО", max_length=100)
    fam = models.CharField("Фамилия", max_length=100)
    name = models.CharField("Имя", max_length=100)
    otch = models.CharField("Отчество", max_length=100)
    born = models.IntegerField("Год. рожд.", null=True, blank=True)
    dolg = models.CharField("Должность", max_length=100)
    password = models.CharField("Пароль", max_length=100, default='1111')
    isAdmin = models.IntegerField("Админ", blank=True, default='0')
    def __str__(self):
        return self.fio

    class Meta:
        ordering = ['fio']
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class MyPers(models.Model):
    myid = models.ForeignKey(Person, related_name='persme', verbose_name="Хозяин", on_delete=models.PROTECT,
                             default=0)
    persid = models.ForeignKey(Person, related_name='persany', verbose_name="Персона", on_delete=models.PROTECT,
                               default=0)

    def __str__(self):
        return self.myid.fio

    class Meta:
        ordering = ['id']
        unique_together = ('myid', 'persid')
        verbose_name = "Список преподавателей"
        verbose_name_plural = "Списки преподавателей"

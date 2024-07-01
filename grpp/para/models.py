from django.db import models

class Para(models.Model):
    name = models.CharField("Название", max_length=100)
    num = models.IntegerField("Номер",default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['num']
        verbose_name = "Пара"
        verbose_name_plural = "Пары"

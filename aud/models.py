from django.db import models

class Aud(models.Model):
    name = models.CharField("Название", max_length=100)
    descr = models.CharField("Описание", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"



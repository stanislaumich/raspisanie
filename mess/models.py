from datetime import datetime

from django.db import models

from person.models import Person


class Mess(models.Model):
    CHOICES = [
        ("0", "ОБЫЧНОЕ"),
        ("1", "ВАЖНОЕ"),
    ]

    dt = models.DateTimeField("Дата", default=datetime.now)
    short = models.CharField("Кратко", max_length=100)
    long = models.CharField("Полно", max_length=255, null=True, blank=True)
    isActive = models.IntegerField("Активно", default=1)
    # warn = models.IntegerField("Важно", default=0)
    warn = models.CharField(
        max_length=1,
        choices=CHOICES,
        default=0,
    )
    fromid = models.ForeignKey(Person, related_name='messmfrom', verbose_name="От кого", on_delete=models.PROTECT,
                               default=0)
    toid = models.ForeignKey(Person, related_name='messto', verbose_name="Кому", on_delete=models.PROTECT, default=0)

    def __str__(self):
        return self.short

    class Meta:
        ordering = ['id']
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

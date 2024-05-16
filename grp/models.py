from django.db import models
class Grp(models.Model):
    num = models.CharField("Номер", max_length=30)
    #fam = models.CharField("Фамилия", max_length=100)
    name = models.CharField("Название", max_length=100)
    #otch = models.CharField("Отчество", max_length=100)
    #born = models.IntegerField("Год. рожд.")
    #dolg = models.CharField("Должность", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
    # Methods
    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])





# Generated by Django 4.2.13 on 2024-06-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mess',
            name='long',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полно'),
        ),
    ]

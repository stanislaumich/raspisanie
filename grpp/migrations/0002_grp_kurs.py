# Generated by Django 4.2.13 on 2024-06-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grpp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grp',
            name='kurs',
            field=models.IntegerField(blank=True, null=True, verbose_name='Курс'),
        ),
    ]

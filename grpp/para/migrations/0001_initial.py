# Generated by Django 4.2.13 on 2024-06-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Para',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('num', models.IntegerField(default=0, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Пара',
                'verbose_name_plural': 'Пары',
                'ordering': ['num'],
            },
        ),
    ]
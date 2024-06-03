# Generated by Django 4.2.13 on 2024-06-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rasp', '0006_alter_person_born'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(null=True, verbose_name='Дата')),
                ('short', models.CharField(max_length=100, verbose_name='Кратко')),
                ('long', models.CharField(max_length=255, verbose_name='Полно')),
                ('isActive', models.IntegerField(default=1, verbose_name='Активно')),
                ('warn', models.IntegerField(default=0, verbose_name='Важно')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'ordering': ['id'],
            },
        ),
    ]
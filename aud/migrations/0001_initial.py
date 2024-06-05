# Generated by Django 4.2.13 on 2024-06-05 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('descr', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Аудитория',
                'verbose_name_plural': 'Аудитории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MyAud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='audany', to='aud.aud', verbose_name='Аудитория')),
                ('myid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='audme', to='person.person', verbose_name='Хозяин')),
            ],
            options={
                'verbose_name': 'Список аудиторий',
                'verbose_name_plural': 'Списки аудиторий',
                'ordering': ['id'],
                'unique_together': {('myid', 'audid')},
            },
        ),
    ]

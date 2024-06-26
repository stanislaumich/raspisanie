# Generated by Django 4.2.13 on 2024-06-10 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MyPredmet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='predmetme', to='person.person', verbose_name='Хозяин')),
                ('predmetid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='predmetany', to='predmet.predmet', verbose_name='Предмет')),
            ],
            options={
                'verbose_name': 'Список предметов',
                'verbose_name_plural': 'Списки предметов',
                'ordering': ['id'],
                'unique_together': {('myid', 'predmetid')},
            },
        ),
    ]

# Generated by Django 4.2.13 on 2024-06-11 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_person_profphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО')),
                ('myid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='persmen', to='person.person', verbose_name='Хозяин')),
                ('persid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='persanyn', to='person.person', verbose_name='Персона')),
            ],
            options={
                'verbose_name': 'Моя заметка',
                'verbose_name_plural': 'Мои заметки',
                'ordering': ['id'],
                'unique_together': {('myid', 'persid')},
            },
        ),
    ]

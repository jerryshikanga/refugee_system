# Generated by Django 2.0 on 2018-07-11 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refugee', '0002_auto_20180711_2148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refugee',
            options={'ordering': ('date_time_registered', 'name'), 'verbose_name': 'Refugee', 'verbose_name_plural': 'Refugees'},
        ),
    ]

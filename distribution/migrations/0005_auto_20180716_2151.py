# Generated by Django 2.0 on 2018-07-16 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0004_auto_20180711_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distribution',
            options={'ordering': ('allocation_time', 'picking_time'), 'permissions': (('can_allocate_distribution', 'Can allocate distribution'), ('can_clear_distribution', 'Can clear distribution')), 'verbose_name': 'Distribution', 'verbose_name_plural': 'Distributions'},
        ),
    ]

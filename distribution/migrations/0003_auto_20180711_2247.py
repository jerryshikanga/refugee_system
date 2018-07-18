# Generated by Django 2.0 on 2018-07-11 19:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('distribution', '0002_distribution_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distribution',
            old_name='time',
            new_name='allocation_time',
        ),
        migrations.AddField(
            model_name='distribution',
            name='picking_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 2.0 on 2018-07-11 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='picture',
            field=models.ImageField(default='profile_default.png', upload_to='accounts/profile/'),
        ),
    ]
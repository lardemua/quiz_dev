# Generated by Django 2.1.7 on 2019-03-24 02:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190324_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

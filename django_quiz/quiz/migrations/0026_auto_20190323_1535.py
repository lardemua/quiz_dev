# Generated by Django 2.1.7 on 2019-03-23 15:35

from django.db import migrations
import quiz.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0025_auto_20190323_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_time',
            field=quiz.models.UnixTimestampField(auto_created=True, null=True),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-20 22:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Quiz')),
            ],
        ),
    ]

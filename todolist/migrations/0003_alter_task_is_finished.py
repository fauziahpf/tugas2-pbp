# Generated by Django 4.1 on 2022-09-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_task_is_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]

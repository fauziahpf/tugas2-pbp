# Generated by Django 4.1 on 2022-09-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0004_alter_mywatchlist_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='watched',
            field=models.CharField(max_length=15),
        ),
    ]

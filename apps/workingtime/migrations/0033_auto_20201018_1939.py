# Generated by Django 3.1.1 on 2020-10-18 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0032_auto_20201016_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
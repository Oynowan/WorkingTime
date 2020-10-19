# Generated by Django 3.1.1 on 2020-10-13 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0027_auto_20201013_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingtime',
            name='start_working_date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2020, 10, 13, 13, 40, 41, 195918)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workingtime',
            name='start_working',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
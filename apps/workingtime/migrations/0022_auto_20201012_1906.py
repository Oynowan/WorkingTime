# Generated by Django 3.1.1 on 2020-10-12 17:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0021_auto_20201012_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingtime',
            name='end_working_corrected',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 17, 6, 42, 49091, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='workingtime',
            name='start_working_corrected',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 12, 17, 6, 42, 49059, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0007_workingtime_worked_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='worked_time',
            field=models.CharField(max_length=255, default='', null=True, blank=True),
        ),
    ]

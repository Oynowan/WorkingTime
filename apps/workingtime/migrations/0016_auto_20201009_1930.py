# Generated by Django 3.1.1 on 2020-10-09 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0015_auto_20201009_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='worked_time',
            field=models.CharField(default='', max_length=255),
        ),
    ]

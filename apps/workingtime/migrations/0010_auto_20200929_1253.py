# Generated by Django 3.1.1 on 2020-09-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0009_auto_20200929_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingtime',
            name='worked_time',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]

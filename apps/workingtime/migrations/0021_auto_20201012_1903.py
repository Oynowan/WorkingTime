# Generated by Django 3.1.1 on 2020-10-12 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0020_remove_workingtime_for_employee_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingtime',
            name='corrected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='workingtime',
            name='worked_time',
            field=models.CharField(default='', max_length=255),
        ),
    ]

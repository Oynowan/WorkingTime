# Generated by Django 3.1.1 on 2020-10-22 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0031_workingtime_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workingtime',
            name='corrected_at',
        ),
        migrations.RemoveField(
            model_name='workingtime',
            name='corrected_by',
        ),
        migrations.RemoveField(
            model_name='workingtime',
            name='notes',
        ),
    ]

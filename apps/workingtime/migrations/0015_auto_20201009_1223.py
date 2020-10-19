# Generated by Django 3.1.1 on 2020-10-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0014_auto_20201001_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingtime',
            name='checked_by_supervisor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workingtime',
            name='is_approved_by_supervisor',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

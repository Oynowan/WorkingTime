# Generated by Django 3.1.1 on 2020-10-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0016_auto_20201009_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fully_registered',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingtime', '0018_auto_20201009_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingtime',
            name='for_employee_info',
            field=models.CharField(default='button is-warning', max_length=30),
        ),
    ]

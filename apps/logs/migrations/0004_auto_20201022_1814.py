# Generated by Django 3.1.1 on 2020-10-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_auto_20201022_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingchangelogs',
            name='notes',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-09 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_auto_20201009_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('unknown', 'unknown'), ('F&B - Restaurant - BFST', 'F&B - Restaurant - BFST'), ('F&B - Restaurant - Evening', 'F&B - Restaurant - Evening'), ('F&B - RoomService - Morning', 'F&B - RoomService - Morning'), ('F&B - RoomService - Evening', 'F&B - RoomService - Evening'), ('F&B - Banket - Morning', 'F&B - Banket - Morning'), ('F&B - Banket - Evening', 'F&B - Banket - Evening')], default='unknown', max_length=100),
        ),
    ]
# Generated by Django 3.1.1 on 2020-10-09 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_userprofile_confirmed_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('unknown', 'unknown'), ('F&amp;B - Restaurant - BFST', 'F&amp;B - Restaurant - BFST'), ('F&B - Restaurant - Evening', 'F&B - Restaurant - Evening'), ('F&B - RoomService - Morning', 'F&B - RoomService - Morning'), ('F&B - RoomService - Evening', 'F&B - RoomService - Evening'), ('F&B - Banket - Morning', 'F&B - Banket - Morning'), ('F&B - Banket - Evening', 'F&B - Banket - Evening')], default='unknown', max_length=100),
        ),
    ]

# Generated by Django 3.1.1 on 2020-10-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='department',
            field=models.CharField(blank=True, choices=[('f&b_restaurant_bfst', 'F&B - Restaurant - BFST'), ('f&b_restaurant_evening', 'F&B - Restaurant - Evening'), ('f&b_roomservice_morning', 'F&B - RoomService - Morning'), ('f&b_roomservice_evening', 'F&B - RoomService - Evening'), ('f&b_banket_morning', 'F&B - Banket - Morning'), ('f&b_banket_evening', 'F&B - Banket - Evening')], max_length=100, null=True),
        ),
    ]
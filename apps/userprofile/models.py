from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # General information's
    name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=25, default='')
    age = models.IntegerField(blank=True, null=True, default=0)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)

    # Departments

    department_choices = (
        ('unknown','unknown'),
        ('F&B - Restaurant - BFST', 'F&B - Restaurant - BFST'),
        ('F&B - Restaurant - Evening', 'F&B - Restaurant - Evening'),
        ('F&B - RoomService - Morning', 'F&B - RoomService - Morning'),
        ('F&B - RoomService - Evening', 'F&B - RoomService - Evening'),
        ('F&B - Banket - Morning', 'F&B - Banket - Morning'),
        ('F&B - Banket - Evening', 'F&B - Banket - Evening'),
    )
    department = models.CharField(max_length=100, choices=department_choices, default='unknown')

    # Variables for tips app
    points = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    money = models.DecimalField(default=0, max_digits=100, decimal_places=2)

    # Variables for workingtime app
    is_valid = models.BooleanField(default=False)
    at_work = models.BooleanField(default=False)
    worked_today = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


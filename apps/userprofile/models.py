from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    money = models.DecimalField(default=0, max_digits=100, decimal_places=2)
    is_valid = models.BooleanField(default=False)
    at_work = models.BooleanField(default=False)
    worked_today = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


from django.db import models
from django.contrib.auth.models import User

from ..userprofile.models import UserProfile
# Create your models here.


class WorkingTime(models.Model):
    users_time = models.ForeignKey(UserProfile, related_name='workingtime', on_delete=models.CASCADE)
    start_working = models.DateTimeField(auto_now_add=True)
    end_working = models.DateTimeField(auto_now_add=True)
    worked_time = models.CharField(max_length=255, null=False)
    done_working = models.BooleanField(default=False)

    class Meta:
        ordering = ('-start_working',)

    def __str__(self):
        return f'{self.users_time.user.username} Date: {self.start_working.month}.{self.start_working.day}'

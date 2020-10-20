from django.db import models
from django.utils import timezone, dateformat
from django.contrib.auth.models import User
from django.contrib.postgres.fields import DateTimeRangeField
import datetime

from apps.userprofile.models import UserProfile
# Create your models here.


class WorkingTime(models.Model):
    users_time = models.ForeignKey(UserProfile, related_name='workingtime', on_delete=models.CASCADE)
    start_working = models.DateTimeField(auto_now_add=True)
    start_working_corrected = models.DateTimeField(default=timezone.now)
    end_working = models.DateTimeField(auto_now_add=True)
    end_working_corrected = models.DateTimeField(auto_now_add=True)
    corrected = models.BooleanField(default=False)

    worked_time = models.CharField(max_length=255, default='', null=True, blank=True)
    worked_time_corrected = models.CharField(max_length=255, default='', null=True, blank=True)
    worked_time_seconds = models.IntegerField(default=0)
    done_working = models.BooleanField(default=False)
    # Supervisor approval
    checked_by_supervisor = models.BooleanField(default=False)
    is_approved_by_supervisor = models.BooleanField(default=False)
    corrected_by = models.CharField(max_length=100, blank=True, null=True)
    corrected_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-start_working',)

    def __str__(self):
        return f'{self.users_time.name} Date: {self.start_working.month}.{self.start_working.day}'

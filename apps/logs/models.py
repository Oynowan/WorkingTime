from django.db import models
from apps.workingtime.models import WorkingTime
# Create your models here.


class WorkingChangeLogs(models.Model):
    workingtime = models.ForeignKey(WorkingTime, related_name='workinglogs', on_delete=models.CASCADE)
    time_changes = models.CharField(max_length=200, null=False, blank=False)

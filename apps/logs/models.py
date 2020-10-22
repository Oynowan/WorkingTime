from django.db import models
from apps.workingtime.models import WorkingTime
# Create your models here.


class WorkingChangeLogs(models.Model):
    workingtime = models.ForeignKey(WorkingTime, related_name='workinglogs', on_delete=models.CASCADE)
    time_start = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    notes = models.CharField(max_length=100, null=False, blank=False)
    changed_by = models.CharField(max_length=60)
    changed_at = models.CharField(max_length=50)

    def __str__(self):
        return self.notes
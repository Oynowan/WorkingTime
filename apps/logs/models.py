from django.db import models
from apps.workingtime.models import WorkingTime
# Create your models here.


class WorkingChangeLogs(models.Model):
    workingtime = models.ForeignKey(WorkingTime, related_name='workinglogs', on_delete=models.CASCADE)
    time_start = models.CharField(max_length=50, default='')
    time_end = models.CharField(max_length=50, default='')
    notes = models.CharField(max_length=100, blank=False, default='')
    changed_by = models.CharField(max_length=60, default='')
    changed_at = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.notes

    class Meta:
        ordering = ('-changed_at',)
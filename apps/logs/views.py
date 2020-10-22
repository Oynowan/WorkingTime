from django.shortcuts import render
from django.shortcuts import get_object_or_404
from ..userprofile.models import UserProfile
from ..workingtime.models import WorkingTime
from ..logs.models import WorkingChangeLogs
from datetime import datetime
import os
import json
# Create your views here.
from ..core.static.decorators import supervisor_member_required


# WorkingTime Logs
@supervisor_member_required()
def wt_logs(request, pk):
    format = '%Y-%m-%d %H:%M'
    working_time = get_object_or_404(WorkingTime, pk=pk)
    path_logs = os.path.abspath(f'apps/logs/templates/logs/download/t_logs/{pk}t_logs/')
    file_log = os.path.abspath(f'apps/logs/templates/logs/download/t_logs/{pk}t_logs/{pk}logs.txt')
    if not os.path.exists(path_logs):
        os.mkdir(path_logs)

    logs_file = open(file_log, 'w')
    logs = WorkingChangeLogs.objects.filter(workingtime=working_time)
    logs_file.write(f'{working_time.users_time.name} {working_time.users_time.last_name} time '
                    f'{datetime.strftime(working_time.start_working_corrected, format)} - '
                    f'{datetime.strftime(working_time.end_working_corrected, format)} - '
                    f'{working_time.worked_time_corrected}\n\n\n')
    for log in logs:
        logs_file.write(f'{log.time_changes}\n\n')
    logs_file.close()
    return render(request, f'{os.path.abspath(f"apps/logs/templates/logs/download/t_logs/{pk}t_logs/{pk}logs.txt")}', {'pk': pk})


# Users all time Logs
@supervisor_member_required()
def u_logs(request, pk):
    format = '%Y-%m-%d %H:%M'
    userprofile = get_object_or_404(UserProfile, pk=pk)
    path_logs = os.path.abspath(f'apps/logs/templates/logs/download/u_logs/{pk}u_logs/')
    file_log = os.path.abspath(f'apps/logs/templates/logs/download/u_logs/{pk}u_logs/{pk}logs.txt')
    if not os.path.exists(path_logs):
        os.mkdir(path_logs)

    logs_file = open(file_log, 'w')
    logs = WorkingTime.objects.filter(users_time=userprofile)
    logs_file.write(f'LOGS: {userprofile.name} {userprofile.last_name}\n\n')
    for log in logs:
        logs_file.write(f'Start: {datetime.strftime(log.start_working, format)}\nEnd: '
                        f'{datetime.strftime(log.end_working, format)}\nWorked Time: '
                        f'{log.worked_time}\n\n')
    logs_file.close()
    return render(request, f'{os.path.abspath(f"apps/logs/templates/logs/download/u_logs/{pk}u_logs/{pk}logs.txt")}', {'pk': pk})


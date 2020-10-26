from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from ..userprofile.models import UserProfile
from ..workingtime.models import WorkingTime
from ..logs.models import WorkingChangeLogs
from datetime import datetime, timedelta
from django.db.models import Q
from django.views.generic import ListView
import os
import pytz
import json
# Create your views here.
from ..core.static.decorators import supervisor_member_required, full_registered


# WorkingTime Logs
@full_registered
@supervisor_member_required
def wt_logs(request, pk):
    format = '%Y-%m-%d %H:%M'
    working_time = get_object_or_404(WorkingTime, pk=pk)
    file_log = os.path.abspath(f'apps/logs/templates/logs/download/t_logs/wt_logs.txt')
    logs_file = open(file_log, 'w')
    logs = WorkingChangeLogs.objects.filter(workingtime=working_time)
    logs_file.write(f'{working_time.users_time.name} {working_time.users_time.last_name} time '
                    f'{datetime.strftime(working_time.start_working_corrected, format)} - '
                    f'{datetime.strftime(working_time.end_working_corrected, format)} - '
                    f'{working_time.worked_time_corrected}\n\n\n')
    for log in logs:
        logs_file.write(f'{log.time_changes}\n\n')
    logs_file.close()
    return render(request, f'{os.path.abspath(f"apps/logs/templates/logs/download/t_logs/wt_logs.txt")}', {'pk': pk})


# Users all time Logs
@full_registered
@supervisor_member_required
def u_logs(request, pk):
    format = '%Y-%m-%d %H:%M'
    userprofile = get_object_or_404(UserProfile, pk=pk)
    # path_logs = os.path.abspath(f'apps/logs/templates/logs/download/u_logs/')
    file_log = os.path.abspath(f'apps/logs/templates/logs/download/u_logs/u_logs.txt')
    # if not os.path.exists(path_logs):
    #    os.mkdir(path_logs)

    logs_file = open(file_log, 'w')
    logs = WorkingTime.objects.filter(users_time=userprofile)
    logs_file.write(f'LOGS: {userprofile.name} {userprofile.last_name}\n\n')
    for log in logs:
        time1_ = log.start_working.astimezone(pytz.timezone('Europe/Berlin'))
        time2_ = log.end_working.astimezone(pytz.timezone('Europe/Berlin'))
        time1 = datetime.strftime(time1_, format)
        time2 = datetime.strftime(time2_, format)
        logs_file.write(f'\nStart: {time1}\nEnd: '
                        f'{time2}\nWorked Time: '
                        f'{log.worked_time}\n\n')
    logs_file.close()
    return render(request, f'{os.path.abspath(f"apps/logs/templates/logs/download/u_logs/u_logs.txt")}', {'pk': pk})

@full_registered
@supervisor_member_required
def daily_logs(request):
    times = WorkingTime.objects.all()
    daily_times = []
    for time in times:
        if time.start_working.day == datetime.now().day:
            daily_times.append(time)
    return render(request, 'logs/daily.html', {'daily_times': daily_times})


@supervisor_member_required()
def weekly_logs(request):
    time_format = "%H:%M"
    kw = request.GET.get('q')
    times = WorkingTime.objects.all()
    users = UserProfile.objects.all()
    times_ = []
    employees = []
    sorted_times = []
    for time in times:
        if datetime.date(time.start_working).strftime('%V') == kw:
            if time.users_time.department == request.user.userprofile.department or request.user.userprofile.manager:
                times_.append(time)
    for time in times_:
        if time.users_time not in employees and not time.users_time.user.is_staff:
            employees.append(time.users_time)
    for employee in employees:
        week_days = ['User', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        week_days[0] = f'{employee.name} {employee.last_name}'
        for time in times_:
            if time.users_time == employee:
                i = 1
                while i <= 7:
                    if datetime.date(time.start_working).strftime('%a') == week_days[i]:
                        time1_ = time.start_working.astimezone(pytz.timezone('Europe/Berlin'))
                        time2_ = time.end_working.astimezone(pytz.timezone('Europe/Berlin'))
                        time1 = datetime.strftime(time1_, time_format)
                        time2 = datetime.strftime(time2_, time_format)
                        week_days[i] = f'{time1} {time2}'
                        break
                    i += 1
        sorted_times.append(week_days)
    for user in users:
        if not user.user.is_staff:
            week_days = ['User', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            if user not in employees:
                if user.department == request.user.userprofile.department or request.user.userprofile.manager:
                    week_days[0] = f'{user.name} {user.last_name}'
                    sorted_times.append(week_days)

    return render(request, 'logs/calendar_week.html', {'kw': kw, 'sorted': sorted_times})


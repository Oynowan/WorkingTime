from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import WorkingTime
from django.contrib.auth.models import User
from ..userprofile.models import UserProfile
from ..core.static.scripts import time_count

# Create your views here.


@login_required()
def working(request):
    if not request.user.userprofile.fully_registered:
        return redirect('user_profile_ui', request.user.username)
    started = 0
    p = User.objects.get(pk=request.user.id)
    time = WorkingTime.objects.filter(users_time=p.userprofile)
    print(len(time))
    if len(time) == 0:
        user = UserProfile.objects.get(user=p)
        user.worked_today = False
        user.at_work = False
        user.save()
        return render(request, 'workingtime/working.html')
    time = time[0]
    if timezone.now().day - time.start_working.day > 0:
        user = UserProfile.objects.get(user=p)
        user.worked_today = False
        user.save()
    worked_time = time.worked_time
    worked = time.start_working.day != timezone.now().day
    start = time.start_working
    context = {
        'start': start,
        'worked': worked,
        'worked_time': worked_time,
        'started': started
    }
    if p.userprofile.at_work:
        started = 1
        context = {
            'start': start,
            'worked': worked,
            'worked_time': worked_time,
            'started': started
        }
        return render(request, 'workingtime/working.html', context)
    return render(request, 'workingtime/working.html', context)


"""@login_required()
def start_working(request):
    if not request.user.userprofile.fully_registered:
        return redirect('user_profile_ui', request.user.username)
    p = User.objects.get(pk=request.user.id)
    user = UserProfile.objects.get(user=p)
    time = user.workingtime.first()
    try:
        if time.end_working != time.start_working and user.at_work is True or user.worked_today is True:
            return render(request, 'core/nope.html')
    except AttributeError:
        pass
    user.at_work = True
    user.save()
    WorkingTime.objects.create(users_time=p.userprofile)
    time = p.userprofile.workingtime.first()
    start = time.start_working
    started = 1
    context = {
        'start': start,
        'started': started
    }
    return render(request, 'workingtime/working.html', context)


@login_required()
def end_working(request):
    if not request.user.userprofile.fully_registered:
        return redirect('user_profile_ui', request.user.username)
    p = UserProfile.objects.get(user=request.user)
    time = p.workingtime.first()
    if time:
        if time.end_working != time.start_working and p.at_work is False:
            return render(request, 'core/nope.html')
    else:
        return render(request, 'core/nope.html')
    startwork = time.start_working
    if p.at_work:
        endwork = timezone.now()
        time.end_working = endwork
        time.done_working = True
        p.worked_today = True
        p.at_work = False
        p.save()
        time.save()
    else:
        endwork = time.end_working
    started = 2
    start = time.start_working
    end = time.end_working
    time.worked_time = time_count(start, end)
    time.save()
    worked_time = time.worked_time
    context = {
        'startwork': startwork,
        'endwork': endwork,
        'worked_time': worked_time,
        'started': started
    }

    return render(request, 'workingtime/working.html', context)
"""


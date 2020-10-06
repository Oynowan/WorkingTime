import json

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import WorkingTime
from ..userprofile.models import User, UserProfile

from ..core.static.scripts import time_count


@login_required()
def api_start_working(request):
    data = json.loads(request.body)
    print('im in api_start_working')
    user = User.objects.get(pk=data['user'])
    user_profile = UserProfile.objects.get(user=user)
    time = user_profile.workingtime.first()
    try:
        if time.end_working != time.start_working and not user.at_work and time.end_working.day == timezone.now().day \
                or user.at_work:
            return render(request, 'core/nope.html')
    except AttributeError:
        pass
    user_profile.at_work = True
    user_profile.save()
    WorkingTime.objects.create(users_time=user_profile)

    return JsonResponse({'success': True})


@login_required()
def api_end_working(request):
    print('im in api_end_working')
    data = json.loads(request.body)
    user = User.objects.get(pk=data['user'])
    user_profile = UserProfile.objects.get(user=user)
    time = user_profile.workingtime.first()
    if time:
        if time.end_working != time.start_working and user_profile.at_work is False:
            return render(request, 'core/nope.html')
    else:
        return render(request, 'core/nope.html')
    if user_profile.at_work:
        time.end_working = timezone.now()
        time.done_working = True
        user_profile.worked_today = True
        user_profile.at_work = False
        user_profile.save()
        time.save()
    start = time.start_working
    end = time.end_working
    min = end - start
    min = min.total_seconds()
    min = f'{min / 60:.0f}'
    time.worked_time = time_count(min)
    time.save()

    return JsonResponse({'success': True})


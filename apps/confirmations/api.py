import json
from django.http import JsonResponse
from apps.userprofile.models import UserProfile
from apps.workingtime.models import WorkingTime
from apps.core.static.decorators import supervisor_member_required
from apps.core.static.scripts import time_count
from django.shortcuts import get_object_or_404
from django.utils import timezone
import datetime
import pytz

@supervisor_member_required
def api_confirmation(request):
    body = json.loads(request.body)
    user = get_object_or_404(UserProfile, pk=int(body['user']))
    account = f'{user}'
    user.checked_account = True
    user.confirmed_employee = body['confirmed']
    user.save()
    return JsonResponse({'message': account}, status=200)


@supervisor_member_required
def api_confirm_time(request, time_id=0):
    body = json.loads(request.body)
    time = get_object_or_404(WorkingTime, pk=int(body['time']))
    s_time = body['s_time'].split(':')
    s_date = body['s_date'].split('-')
    now = datetime.datetime.now()
    correct_s = now.replace(year=int(s_date[0]),
                            month=int(s_date[1]),
                            day=int(s_date[2]),
                            hour=int(s_time[0]),
                            minute=int(s_time[1]),
                            second=00,
                            microsecond=00, tzinfo=pytz.utc)
    print(correct_s)
    return JsonResponse({'success': True}, status=200)

from django.shortcuts import render, redirect, get_object_or_404
from apps.userprofile.models import UserProfile
from apps.workingtime.models import WorkingTime
from ..core.static.decorators import supervisor_member_required
from django.utils import timezone
from django.db.models import Q
# Create your views here.


@supervisor_member_required()
def to_confirm(request):
    to_confirm_employees = UserProfile.objects.filter(Q(checked_account=False), Q(fully_registered=True))
    return render(request, 'confirmations/to_confirm.html', {'to_confirm': to_confirm_employees})


@supervisor_member_required()
def to_confirm_time(request):
    # to_confirm_times = WorkingTime.objects.filter(Q(checked_by_supervisor=False), Q(done_working=True))
    return render(request, 'confirmations/to_confirm_time.html')


@supervisor_member_required()
def correcting_time(request, time_id):
    working = get_object_or_404(WorkingTime, pk=int(time_id))
    s_working = timezone.localtime(working.start_working)
    e_working = timezone.localtime(working.end_working)
    context = {
        'working': working,
        'time_id': time_id,
        'stime': s_working,
        'etime': e_working
    }
    return render(request, 'confirmations/correcting_time.html', context)

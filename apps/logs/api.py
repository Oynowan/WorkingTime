from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json
from .models import WorkingChangeLogs
from ..workingtime.models import WorkingTime
from ..core.static.decorators import supervisor_member_required


@supervisor_member_required()
def api_workingtime_change_logs(request):
    data = json.loads(request.body)
    workingtime = get_object_or_404(WorkingTime, pk=data['pk'])
    change_logs = WorkingChangeLogs.objects.filter(workingtime=workingtime)
    change_logs_ = []
    for change in change_logs:
        change_logs_.append(change)
        print(change)
    context = {
        'logs': True
    }

    return JsonResponse(context)
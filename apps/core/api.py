from django.http import JsonResponse
import json
from apps.userprofile.models import UserProfile
from apps.workingtime.models import WorkingTime
from .static.decorators import supervisor_member_required


class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
        sort_keys=True, indent=4)


@supervisor_member_required()
def api_get_not_confirmed_yet(request):
    not_confirmed = UserProfile.objects.filter(confirmed_employee=False)
    number_not_confirmed = len(not_confirmed)
    return JsonResponse({'number_not_confirmed': number_not_confirmed}, status=200)


@supervisor_member_required()
def api_get_not_confirmed_time(request):
    not_confirmed = WorkingTime.objects.filter(checked_by_supervisor=False)
    number_not_confirmed = len(not_confirmed)
    print(number_not_confirmed)
    return JsonResponse({'number_not_confirmed': number_not_confirmed}, status=200)

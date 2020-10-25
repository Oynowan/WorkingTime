import json, re

from django.http import JsonResponse
from django.utils.safestring import mark_safe

from .models import UserProfile, User


def api_save_profile_changes(request):
    email_check = r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]' \
                  r'{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

    body = json.loads(request.body)
    if request.user.userprofile.supervisor:
        user_u = User.objects.get(username=body['user'])
        user = UserProfile.objects.get(user=user_u)
        user.confirmed_employee = body['confirmed']
        if body['confirmed']:
            user.checked_account = True
    else:
        user = UserProfile.objects.get(user=request.user)
    if body['name'] == '' or body['last_name'] == '' or body['department'] == 'Unspecify':
        user.fully_registered = False
    else:
        user.fully_registered = True
    if request.user.userprofile.manager:
        user.supervisor = body['confirmed_supervisor']
        if body['confirmed_supervisor']:
            user.confirmed_employee = True
            user.checked_account = True
    user.name = body['name']
    user.last_name = body['last_name']
    user.department = mark_safe(body['department'])
    email = UserProfile.objects.filter(email=body['email'])
    if len(email) > 0 and email[0].user.pk != user.user.pk or not re.match(email_check, body['email']):
        wrong_email = True
    else:
        wrong_email = False
        user.email = body['email']
    if body['age'] is not None:
        user.age = body['age']
    user.save()

    return JsonResponse({'success': True, 'email': wrong_email})

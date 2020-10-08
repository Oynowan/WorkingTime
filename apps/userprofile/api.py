import json

from django.http import JsonResponse

from .models import UserProfile


def api_save_profile_changes(request):

    body = json.loads(request.body)
    user = UserProfile.objects.get(user=request.user)
    user.name = body['name']
    user.last_name = body['last_name']
    email = UserProfile.objects.filter(email=body['email'])
    if len(email) > 0 and email[0].user.pk != user.user.pk:
        wrong_email = True
    else:
        wrong_email = False
        user.email = body['email']
    if body['age'] is not None:
        user.age = body['age']
    user.save()

    return JsonResponse({'success': True, 'email': wrong_email})

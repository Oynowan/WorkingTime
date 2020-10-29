from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import WorkingTime
from django.contrib.auth.models import User
from ..userprofile.models import UserProfile
from ..core.static.scripts import time_count
from ..core.static.decorators import full_registered

# Create your views here.


@login_required
@full_registered
def working(request):
    p = User.objects.get(pk=request.user.id)
    time = p.userprofile.workingtime.first()

    if not time:
        user = UserProfile.objects.get(user=p)
        user.worked_today = False
        user.at_work = False
        user.save()
        return render(request, 'core/frontpage.html')
    if timezone.now().day - time.start_working.day > 0:
        user = UserProfile.objects.get(user=p)
        user.worked_today = False
        user.save()
    return render(request, 'core/frontpage.html')

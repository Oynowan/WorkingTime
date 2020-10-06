from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.
from ..workingtime.models import WorkingTime
from .static.scripts import time_count
from ..userprofile.models import UserProfile

from django.http import HttpResponseRedirect


def frontpage(request):
    if request.user.is_authenticated:
        work_dates = WorkingTime.objects.filter(users_time=request.user.userprofile)
    else:
        work_dates = ['AnonymousUser']
    try:
        if work_dates[0]:
            lazy = True
    except IndexError:
        lazy = False
    context = {
        'work_dates': work_dates,
        'lazy': lazy,
    }
    return render(request, 'core/frontpage.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})


def delete_workingtime(request):
    time = WorkingTime.objects.get(pk=int(request.POST['delete']))
    user = UserProfile.objects.get(user=request.user)
    user.at_work = False
    user.save()
    time.delete()
    return redirect('frontpage')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..workingtime.models import WorkingTime
from .static.scripts import time_count
from .static.scripts import check_registered
from ..userprofile.models import UserProfile, User
from .forms import CreateUserForm
from django.db.models import Q
from django.views.generic import ListView
from .static.decorators import unauthenticated_user, full_registered
from django.utils import timezone
from datetime import timedelta, datetime


@unauthenticated_user
def basepage(request):
    return render(request, 'core/base.html')


@login_required
def frontpage(request):
    if request.user.is_authenticated:
        if not request.user.userprofile.fully_registered:
            return redirect('user_profile_ui', request.user.username)
        work_dates = WorkingTime.objects.filter(users_time=request.user.userprofile)
        total_time = 0
        for work in work_dates:
            total_time += work.worked_time_seconds
        hour = 0
        while total_time >= 60:
            hour += 1
            total_time -= 60
        total_time_ = f'{hour}h {total_time}min'
    else:
        work_dates = ['AnonymousUser']
        total_time_ = '00:00'
    context = {
        'work_dates': work_dates,
        'total_time': total_time_
    }

    p = User.objects.get(pk=request.user.id)
    time = p.userprofile.workingtime.first()

    if not time:
        user = UserProfile.objects.get(user=p)
        user.worked_today = False
        user.at_work = False
        user.save()
        return render(request, 'core/frontpage.html')
    today = datetime.strftime(timezone.now(), '%Y-%m-%d')
    last_day = datetime.strftime((time.start_working + timedelta(days=1)), '%Y-%m-%d')
    print(today, last_day)
    if today >= last_day:
        user = UserProfile.objects.get(user=p)
        user.worked_today = False
        user.save()
    return render(request, 'core/frontpage.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('frontpage')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            messages.info(request, 'Wrong Username or Password')
    context = {}
    return render(request, 'core/login.html', context)


@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile_ui', user.username)
        else:
            print(form.errors)
    else:
        form = CreateUserForm()

    return render(request, 'core/signup.html', {'form': form})


class SearchResultView(ListView):
    model = UserProfile
    template_name = 'list_of_users.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = []
        if ' ' in query:
            query_ = query.split(' ')
            for q in query_:
                object_lists = UserProfile.objects.filter(
                    Q(name__icontains=q) | Q(last_name__icontains=q)
                    )
                object_list.append(object_lists)
        else:
            object_list.append(UserProfile.objects.filter(Q(name__icontains=query) | Q(last_name__icontains=query)))
        is_valid_ = object_list[0].exists()
        return {'object_list': object_list, 'query': query, 'is_valid': is_valid_}



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from ..workingtime.models import WorkingTime
from .static.scripts import time_count
from .static.scripts import check_registered
from ..userprofile.models import UserProfile
from django.db.models import Q
from django.views.generic import ListView


def frontpage(request):
    if request.user.is_authenticated:
        if not request.user.userprofile.fully_registered:
            return redirect('user_profile_ui', request.user.username)
        work_dates = WorkingTime.objects.filter(users_time=request.user.userprofile)
    else:
        work_dates = ['AnonymousUser']
    try:
        if work_dates[0]:
            lazy = True
    except IndexError:
        lazy = False

    to_confirm = UserProfile.objects.filter(Q(checked_account=False), Q(fully_registered=True))
    to_confirm_time = WorkingTime.objects.filter(Q(checked_by_supervisor=False), Q(done_working=True))
    context = {
        'work_dates': work_dates,
        'lazy': lazy,
        'to_confirm_num': len(to_confirm),
        'to_confirm_time': len(to_confirm_time)

    }
    return render(request, 'core/frontpage.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile_ui', user.username)
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})


def delete_workingtime(request):
    if not request.user.userprofile.fully_registered:
        redirect('user_profile_ui', request.user.username)
    print('Im here')
    time = WorkingTime.objects.get(pk=int(request.POST['delete']))
    user = UserProfile.objects.get(user=request.user)
    user.at_work = False
    user.save()
    time.delete()
    return redirect('frontpage')


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

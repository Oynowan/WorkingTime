from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def user_profile_ui(request, user):
    if user != request.user.username:
        return redirect('frontpage')
    context = {
        'user': user,
        'user_profile': request.user.userprofile
    }
    return render(request, 'userprofile/userprofile.html', context)

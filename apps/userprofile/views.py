from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.


@login_required()
def user_profile_ui(request, user):
    user_u = get_object_or_404(User, username=user)
    change_password = PasswordChangeForm(user_u)
    department_choices = user_u.userprofile.department_choices
    if user != request.user.username:
        if user_u.is_staff and not request.user.is_staff:
            return redirect('frontpage')
        if not request.user.userprofile.supervisor:
            return redirect('frontpage')
    context = {
        'user': user,
        'user_profile': user_u.userprofile,
        'change_password': change_password
    }

    if request.method == 'POST':
        form = PasswordChangeForm(user_u, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfuly updated!')
        else:
            messages.error(request, 'Please correct that error below.')
    return render(request, 'userprofile/userprofile.html', context)

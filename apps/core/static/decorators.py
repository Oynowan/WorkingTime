from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect


def supervisor_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                               login_url='frontpage'):

    """
    Decorator for views that checks that the user is logged in and is a supervisor
    member, redirecting to the frontpage if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.userprofile.supervisor,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('frontpage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def full_registered(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.userprofile.fully_registered or not request.user.userprofile.confirmed_employee:
                return redirect('user_profile_ui', request.user.username)
            else:
                return view_func(request, *args, **kwargs)
    return wrapper_func
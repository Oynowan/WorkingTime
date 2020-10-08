from django.shortcuts import render, redirect
from ..userprofile.models import User, UserProfile
from django.contrib.admin.views.decorators import staff_member_required
from ..core.static.scripts import check_registered
# Create your views here.


@staff_member_required()
def views_employees(request):
    if check_registered(request.user.userprofile):
        return redirect('user_profile_ui', request.user.username)
    all = UserProfile.objects.all()
    employees = []
    for employee in all:
        if not employee.user.username == 'admin' and not employee.name == '' and not employee.last_name == '':
            employees.append(employee)
    return render(request, 'tips/tips.html', {'employees': employees})


@staff_member_required()
def tips_shared(request):
    if check_registered(request.user.userprofile):
        return redirect('user_profile_ui', request.user.username)
    points = 0
    money = float(request.POST['money'])
    total = 0
    for input in request.POST:
        if 'points' in input:
            user = UserProfile.objects.get(pk=int(input[6:]))
            user.points = request.POST[input]
            user.save()
            points += float(request.POST[input])
    if points != 0:
        avg_money = money / points
    else:
        avg_money = 0
    employees = UserProfile.objects.all()
    list_of_employees = []
    for employee in employees:
        if not employee.user.username == 'admin' and not employee.name == '' and not employee.last_name == '':
            list_of_employees.append(employee)
            employee.money = round(float(employee.points) * avg_money, 0)
            employee.points = 0
            employee.save()
            total += employee.money
    context = {
        'employees': list_of_employees,
        'rest': money - total,
    }
    return render(request, 'tips/tips_shared.html', context)

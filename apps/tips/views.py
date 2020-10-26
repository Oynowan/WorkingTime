from django.shortcuts import render, redirect
from ..userprofile.models import User, UserProfile
from django.contrib.admin.views.decorators import staff_member_required
from ..core.static.decorators import supervisor_member_required, full_registered
from ..core.static.scripts import check_registered
# Create your views here.

@full_registered
@supervisor_member_required()
def views_employees(request):
    if not request.user.userprofile.fully_registered:
        return redirect('user_profile_ui', request.user.username)
    all = UserProfile.objects.all()
    supervisor = request.user.userprofile
    employees = []
    for employee in all:
        if employee.confirmed_employee and employee.department == supervisor.department and not employee.user.is_staff:
            employees.append(employee)
    return render(request, 'tips/tips.html', {'employees': employees})

@full_registered
@supervisor_member_required()
def tips_shared(request):
    if not request.user.userprofile.fully_registered:
        return redirect('user_profile_ui', request.user.username)
    if len(request.POST) == 0:
        return render(request, 'core/nope.html')
    points = 0
    money = float(request.POST['money'])
    total = 0
    supervisor = request.user.userprofile
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
        if employee.confirmed_employee and employee.department == supervisor.department and not employee.user.is_staff:
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

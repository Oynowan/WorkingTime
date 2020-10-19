from django.shortcuts import redirect
import datetime

# Counts working time and converts to hours/minutes


def time_count(start, end):

    time_delta = end - start
    if time_delta.days < 0:
        return ['You cant finish work before start', 0]
    days, seconds = time_delta.days, time_delta.total_seconds()
    print(days, seconds, time_delta)
    days = days * 1440
    minutes = seconds // 60
    total_minutes_ = days+minutes
    total_minutes = total_minutes_
    print(time_delta)
    print(total_minutes)
    hour = 0
    while int(total_minutes) >= 60:
        hour += 1
        total_minutes = int(total_minutes) - 60
    if hour > 0:
        return [f'{hour}h {total_minutes}min', total_minutes_]
    else:
        return [f'{total_minutes}min', total_minutes_]


# Checks if user completed registration
def check_registered(user):
    return user.name == '' or user.last_name == '' or user.department == 'Unspecify'

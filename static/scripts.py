from django.shortcuts import redirect


# Counts working time and converts to hours/minutes
def time_count(start, end):
    print(end, start)
    minutes = end - start
    print(minutes)
    minutes = minutes.total_seconds()
    print(minutes)
    minutes = round(minutes/60)
    hour = 0
    while int(minutes) >= 60:
        hour += 1
        minutes = int(minutes) - 60
    if hour > 0:
        return f'{hour}h {minutes}min'
    else:
        return f'{minutes}min'


# Checks if user completed registration
def check_registered(user):
    return user.name == '' or user.last_name == '' or user.department == 'Unspecify'

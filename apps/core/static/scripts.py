from django.shortcuts import redirect


# Counts working time and converts to hours/minutes
def time_count(time):
    min = time
    hour = 0
    while int(min) >= 60:
        hour += 1
        min = int(min) - 60
    if hour > 0:
        return f'{hour}h {min}min'
    else:
        return f'{min}min'


# Checks if user completed registration
def check_registered(user):
    return user.name == '' or user.last_name == ''

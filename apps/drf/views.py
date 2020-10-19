from django.shortcuts import render
from .permissions import IsOwnerSupervisorOrReadOnlyUserProfile, IsOwnerSupervisorOrReadOnlyWorkingTime
from .serializers import WorkingTimeSerializer, UserProfileSerializer
# Workingtime app
from ..workingtime.models import WorkingTime
# Userprofile app
from ..userprofile.models import UserProfile
# RestFramework
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import generics
from rest_framework.reverse import reverse
from ..core.static.scripts import time_count
import pytz
from datetime import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404
import json
import io
from datetime import timedelta
# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('userprofile-list', request=request, format=format),
        'workingtime': reverse('workingtime-list', request=request, format=format)
    })


class WorkingTimeList(generics.ListCreateAPIView):
    queryset = WorkingTime.objects.all()
    serializer_class = WorkingTimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(users_time=self.request.user.userprofile)


class WorkingTimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkingTime.objects.all()
    serializer_class = WorkingTimeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerSupervisorOrReadOnlyWorkingTime]

    def update(self, request, *args, **kwargs):
        workingtime = self.get_object()
        user = get_object_or_404(UserProfile, pk=workingtime.users_time.pk)
        tz = pytz.timezone('Poland')
        time_format = "%Y-%m-%d %H:%M:%S"
        if request.data['ending_work']:
            workingtime.done_working = True
            user.at_work = False
            user.worked_today = True
            user.save()
            time = time_count(workingtime.start_working, timezone.now())

            if time[1] > 600:
                end_work = workingtime.start_working + timedelta(hours=10)
                workingtime.end_working = end_work
                workingtime.worked_time = 'Worked to much, default time added. 10h'
            elif time[1] < 0:
                print('cant work into the past')
                return Response({'over': True, 'success': True})
            else:
                if request.data['break']:
                    print(request.data['break'])
                    end = timezone.now() + timedelta(minutes=30)
                    print('end')
                    time = time_count(workingtime.start_working, end)
                    workingtime.end_working = end
                else:
                    workingtime.end_working = timezone.now()
                workingtime.worked_time = time[0]
                workingtime.worked_time_seconds = time[1]
        else:
            # If time was checked by supervisor but not approved
            if request.data['checked_by_supervisor'] and not request.data['is_approved_by_supervisor']:
                time1_ = request.data['start_working'].replace('T', ' ')
                time2_ = request.data['end_working'].replace('T', ' ')
                time1 = datetime.strptime(time1_, time_format)
                time2 = datetime.strptime(time2_, time_format)
                time = time_count(time1, time2)
                utc_time1 = tz.localize(time1, is_dst=None).astimezone(pytz.utc)
                utc_time2 = tz.localize(time2, is_dst=None).astimezone(pytz.utc)
                total_minutes = time_count(time1, time2)

                if total_minutes[1] <= 0:
                    return Response({'over': True, 'success': True})
                workingtime.worked_time_seconds = total_minutes[1]
                workingtime.start_working_corrected = workingtime.start_working
                workingtime.end_working_corrected = workingtime.end_working
                workingtime.start_working = utc_time1
                workingtime.end_working = utc_time2
                workingtime.worked_time_corrected = workingtime.worked_time
                workingtime.worked_time = total_minutes[0]
                workingtime.checked_by_supervisor = True
                workingtime.corrected = True
                workingtime.corrected_by = f'{request.user.userprofile.name} {request.user.userprofile.last_name}'
                workingtime.corrected_at = timezone.now()

            # If time was checked by supervisor and approved
            elif request.data['checked_by_supervisor'] and request.data['is_approved_by_supervisor']:
                workingtime.checked_by_supervisor = True
                workingtime.is_approved_by_supervisor = True

        workingtime.save()
        return Response({'over': False, 'success': True})


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(users_time=self.request.user.userprofile)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerSupervisorOrReadOnlyUserProfile]

    def update(self, request, *args, **kwargs):
        userprofile = self.get_object()

        if request.data['at_work']:
            userprofile.at_work = True
        else:
            userprofile.at_work = False
            userprofile.worked_today = True
        userprofile.save()

        return Response({'success': True})

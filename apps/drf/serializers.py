from rest_framework import serializers
from ..workingtime.models import WorkingTime
from ..userprofile.models import UserProfile


class WorkingTimeSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='users_time.user.username')
    users_time = serializers.HyperlinkedRelatedField(many=False, view_name='userprofile-detail', read_only=True)
    name = serializers.ReadOnlyField(source='users_time.name')
    last_name = serializers.ReadOnlyField(source='users_time.last_name')
    start_working = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    end_working = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    start_working_corrected = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_working_corrected = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    corrected_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = WorkingTime
        fields = ['id', 'users_time', 'owner', 'start_working', 'start_working_corrected', 'end_working',
                  'end_working_corrected', 'corrected', 'worked_time', 'worked_time_corrected', 'done_working',
                  'checked_by_supervisor', 'is_approved_by_supervisor', 'name', 'last_name', 'corrected_by',
                  'corrected_at', 'worked_time_seconds']


class UserProfileSerializer(serializers.ModelSerializer):

    workingtime = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'id', 'name', 'last_name', 'workingtime', 'age', 'email', 'fully_registered',
                  'checked_account', 'confirmed_employee', 'supervisor', 'department', 'points', 'money',
                  'is_valid', 'at_work', 'worked_today']


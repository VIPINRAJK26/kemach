from rest_framework import serializers
from .models import Machinery, TestDrive

class MachinerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Machinery
        fields = ['id', 'name', 'description', 'available_for_test_drive']

class TestDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDrive
        fields = ['user', 'machinery', 'test_drive_date']

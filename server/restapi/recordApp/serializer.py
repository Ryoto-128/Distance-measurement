from rest_framework import serializers

from .models import Facility, DistanceRecord


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ('facility_id', 'name', 'total_area', 'seats_area', 'waitting_area', 'seats_num')

    def create(self, validated_data):
        return Facility.objects.create_Facility(request_data = validated_data)
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.save()
        return instance


class DistanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistanceRecord
        fields = ('facility_id', 'status', 'created_at',
                  'guests_num', 'avg_distance')

    def create(self, validated_data):
        return DistanceRecord.objects.create_DistanceRecord(request_data = validated_data)
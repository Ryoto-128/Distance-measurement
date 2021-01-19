from django.db import models
from django.utils import timezone

# Create your models here.


class FacilityManager(models.Manager):
    def create_Facility(self, request_data):
        if not request_data[facility_id]:
            raise ValueError('The given facility_id must be set')
        if not request_data[total_area]:
            raise ValueError('The given name must be set')
        if not request_data[seats_area]:
            raise ValueError('The given seats_area must be set')
        if not request_data[waitting_area]:
            raise ValueError('The given waitting_area must be set')
        if not request_data[seats_num]:
            raise ValueError('The given seats_num must be set')

        facility = Facility(
            facility_id = request_data["facility_id"],
            name = request_data["name"],
            total_area = request_data["total_area"],
            seats_area = request_data["seats_area"],
            waitting_area = request_data["waitting_area"],
            seats_num = request_data["seats_num"],
        )
        facility.save(using=self._db)
        return facility


class Facility(models.Model):
    facility_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    total_area = models.FloatField()
    seats_area = models.FloatField()
    waitting_area = models.FloatField()
    seats_num = models.IntegerField()
    
    objects = FacilityManager()



class DistanceRecordManager(models.Manager):
    def create_DistanceRecord(self, request_data, **extra_fields):
        if not request_data["facility_id"]:
            raise ValueError('The given facility_id must be set')
        if not request_data["status"]:
            raise ValueError('The given name must be set')
        if not request_data["guests_num"]:
            raise ValueError('The given guests_num must be set')
        if not request_data["avg_distance"]:
            raise ValueError('The given avg_distance must be set')
        distance_record = DistanceRecord(
            facility_id = request_data["facility_id"],
            status = request_data["status"],
            guests_num = request_data["guests_num"],
            avg_distance = request_data["avg_distance"],
        )
        distance_record.save(using=self._db)
        return distance_record

class DistanceRecord(models.Model):
    STATUS_OPEN = "open"
    STATUS_CLOSE = "close"
    STATUS_SET = (
        (STATUS_OPEN, "開店中"),
        (STATUS_CLOSE, "閉店中"),
    )

    facility_id = models.ForeignKey(
        Facility, related_name='distance_recode', on_delete=models.CASCADE)
    status = models.CharField(
        choices=STATUS_SET, default=STATUS_CLOSE, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    guests_num = models.IntegerField()
    avg_distance = models.FloatField()
    
    objects = DistanceRecordManager()

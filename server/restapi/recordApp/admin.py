from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Facility, DistanceRecord


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass

@admin.register(DistanceRecord)
class DistanceRecord(admin.ModelAdmin):
    pass
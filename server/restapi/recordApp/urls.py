from django.urls import path
from django.conf.urls import url, include

from .views import FacilityRegister, FacilityGetInfoView, FacilityUpdateView, DistanceRecordUpload, DistanceRecordGetRecord

urlpatterns = [
    url(r'^register/', FacilityRegister.as_view()),
    url(r'^get-info/', FacilityGetInfoView.as_view()),
    url(r'^update/', FacilityUpdateView.as_view()),
    url(r'^upload', DistanceRecordUpload.as_view()),
    url(r'^get-record', DistanceRecordGetRecord.as_view()),
]

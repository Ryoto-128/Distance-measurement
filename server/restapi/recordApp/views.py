from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.db import transaction
from django.http import HttpResponse, Http404
from rest_framework import authentication, permissions, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView

from .models import Facility, DistanceRecord
from .serializer import FacilitySerializer, DistanceRecordSerializer


class FacilityRegister(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = FacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacilityGetInfoView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    filter_fields = ('facility_id',)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = FacilitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FacilityUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FacilitySerializer
    lookup_field = 'facility_id'
    queryset = Facility.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(
                facility_id=self.request.data["facility_id"])
            return instance
        except User.DoesNotExist:
            raise Http404


# deleate

# class FacilityDeleteView(generics.DestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = FacilitySerializer
#     lookup_field = 'facility_id'
#     queryset = Facility.objects.all()

#     def get_object(self):
#         try:
#             instance = self.queryset.get(facility_id=self.request.data["facility_id"])
#             return instance
#         except Facility.DoesNotExist:
#             raise HTTP_404


class DistanceRecordUpload(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = DistanceRecord.objects.all()
    serializer_class = DistanceRecordSerializer

    @transaction.atomic
    def post(self, request, format=None):
        serializer = DistanceRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistanceRecordGetRecord(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = DistanceRecord.objects.all()
    serializer_class = DistanceRecordSerializer
    filter_fields = 'facility_id', 'status', 'created_at', 'guests_num', 'avg_distance'

    def list(self, request):
        queryset = self.get_queryset()
        serializer = DistanceRecordSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# deleate
# class DistanceRecordDeleteView(generics.DestroyAPIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = DistanceRecordSerializer
#     lookup_field = 'facility_id'
#     queryset = DistanceRecord.objects.all()

#     def get_object(self):
#         try:
#             instance = self.queryset.get(facility_id=self.request.data["facility_id"])
#             return instance
#         except DistanceRecord.DoesNotExist:
#             raise HTTP_404

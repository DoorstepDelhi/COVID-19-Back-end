from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from django.db.models import Q
import datetime

from .models import (
    State,
    City,
    Facility,
    Service,
    Hospital,
    Volunteer,
    Experience,
    Plasma,
    Request,
)
from .serializers import (
    StateSerializer,
    CitySerializer,
    FacilitySerializer,
    ServiceSerializer,
    HospitalSerializer,
    VolunteerSerializer,
    ExperienceSerializer,
    PlasmaSerializer,
    RequestSerializer,
)
from .permission import IsAdminOrReadOnly, IsStaffOrReadOnly, ReadOrPostOnly


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = State.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = City.objects.filter(verified=True)


class FacilityViewSet(viewsets.ModelViewSet):
    serializer_class = FacilitySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Facility.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly, IsStaffOrReadOnly]

    def get_queryset(self):
        queryset = Service.objects.all().order_by('-verified', '-updated_at')
        if self.request.query_params.get("search", None):
            search = self.request.query_params.get("search", None)
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(address__icontains=search)| Q(note__icontains=search)| Q(mobile__icontains=search)
            )

        if self.request.query_params.get("cities", None):
            cities = self.request.query_params.get("cities", None)
            queryset = queryset.filter(city__icontains__in = cities)

        if self.request.query_params.get("facilities", None):
            facilities = self.request.query_params.get("facilities", None)
            queryset = queryset.filter(facility__icontains__in = facilities)

        if self.request.query_params.get("city", None):
            city = self.request.query_params.get("city", None)
            queryset = queryset.filter(city__icontains = city)

        if self.request.query_params.get("facility", None):
            facility = self.request.query_params.get("facility", None)
            queryset = queryset.filter(facility__icontains = facility)
        return queryset


class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    permission_classes = [IsAdminOrReadOnly, IsStaffOrReadOnly]
    queryset = Hospital.objects.order_by('-verified')


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    permission_classes = [IsAdminOrReadOnly, IsStaffOrReadOnly]
    queryset = Volunteer.objects.order_by('-verified')


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = [ReadOrPostOnly]

    def get_queryset(self):
        queryset = Experience.objects.all().order_by('-verified', '-updated_at')
        return queryset


class PlasmaViewSet(viewsets.ModelViewSet):
    serializer_class = PlasmaSerializer
    permission_classes = [ReadOrPostOnly]
    queryset = Plasma.objects.all().order_by('-verified', '-updated_at')


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    permission_classes = [ReadOrPostOnly]
    queryset = Request.objects.all().order_by('-created_at')

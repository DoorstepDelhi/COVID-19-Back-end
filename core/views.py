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
)
from .serializers import (
    StateSerializer,
    CitySerializer,
    FacilitySerializer,
    ServiceSerializer,
    HospitalSerializer,
    VolunteerSerializer,
    ExperienceSerializer,
)
from .permission import IsAdminOrReadOnly, IsStaffOrReadOnly, ReadOrPostOnly


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = State.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = City.objects.all()


class FacilityViewSet(viewsets.ModelViewSet):
    serializer_class = FacilitySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Facility.objects.all()


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly, IsStaffOrReadOnly]
    queryset = Service.objects.all()


class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class = HospitalSerializer
    permission_classes = [IsAdminOrReadOnly, IsStaffOrReadOnly]
    queryset = Hospital.objects.all()


class VolunteerViewSet(viewsets.ModelViewSet):
    serializer_class = VolunteerSerializer
    permission_classes = [IsAdminOrReadOnly, IsStaffOrReadOnly]
    queryset = Volunteer.objects.all()


class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = [ReadOrPostOnly]
    queryset = Experience.objects.all()

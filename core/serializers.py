from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import (
    State,
    City,
    Facility,
    Service,
    Hospital,
    Volunteer,
    Experience,
)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = City
        fields = ['id', 'state', 'name', 'verified']


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'name', 'description', 'deliver']


class ServiceSerializer(serializers.ModelSerializer):
    cities_list = serializers.SerializerMethodField(read_only=True)
    facilities_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Service
        fields = [
            'id',
            'city',
            'facility',
            'name',
            'contact_person',
            'mobile',
            'alternate_mobile',
            'address',
            'verified',
            'note',
            'lat',
            'long',
            'deliver_at_doorstep',
            'updated_at',
            'created_at',
            'requested_verification',
            'emergency_contact',
            'opening_time',
            'closing_time',
            'request_edit',
            'edit',
            'cities_list',
            'facilities_list',
        ]

    def get_cities_list(self, obj):
        cities = obj.city.all().values_list("name", flat=True)
        return cities

    def get_facilities_list(self, obj):
        facilities = obj.facility.all().values_list("name", flat=True)
        return facilities

    def get_experiences(self, obj):
        experiences = Experience.objects.filter(service=obj)
        serializer = ExperienceSerializer(experiences, many=True)
        return serializer.data


class HospitalSerializer(serializers.ModelSerializer):
    cities_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Hospital
        fields = [
            'id',
            'city',
            'name',
            'mobile',
            'alternate_mobile',
            'address',
            'verified',
            'lat',
            'long',
            'total_oxygen_beds',
            'total_ventilators',
            'total_icu',
            'available_oxygen_beds',
            'available_ventilators',
            'available_icu',
            'updated_at',
            'created_at',
            'requested_verification',
            'emergency_contact',
            'opening_time',
            'closing_time',
            'request_edit',
            'edit',
            'cities_list',
        ]

    def get_cities_list(self, obj):
        cities = obj.city.all().values_list("name", flat=True)
        return cities


class VolunteerSerializer(serializers.ModelSerializer):
    cities_list = serializers.SerializerMethodField(read_only=True)
    facilities_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Volunteer
        fields = [
            'id',
            'user',
            'city',
            'name',
            'mobile',
            'alternate_mobile',
            'facilities',
            'available_from',
            'available_till',
            'verified',
            'created_at',
            'note',
            'cities_list',
            'facilities_list',
        ]


    def get_cities_list(self, obj):
        cities = obj.city.all().values_list("name", flat=True)
        return cities

    def get_facilities_list(self, obj):
        facilities = obj.facility.all().values_list("name", flat=True)
        return facilities


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id',
            'service',
            'name',
            'mobile',
            'alternate_mobile',
            'experience',
            'experienced_on',
            'created_at',
            'visible',
            'available',
        ]




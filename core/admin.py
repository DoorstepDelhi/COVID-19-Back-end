from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    State,
    City,
    Facility,
    Service,
    Hospital,
    Experience
)


class CityAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'state',
                    'verified',
                    ]
    list_editable = [
                    'verified',
                    ]
    list_display_links = [
                    'name',
                    'state',
                    ]
    list_filter = [
                    'state',
                    ]
    search_fields = [
                    'name',
                    'state',
                    ]


class FacilityAdmin(ImportExportModelAdmin):
    list_display = [
        'name',
        'deliver',
    ]
    list_editable = [
        'deliver',
    ]
    list_display_links = [
        'name',
    ]
    list_filter = [
        'deliver',
    ]
    search_fields = [
        'name',
        'description',
    ]


class ServiceAdmin(ImportExportModelAdmin):
    list_display = [
        'name',
        'mobile',
        'verified',
        'deliver_at_doorstep',
        'updated_at',
        'requested_verification',
        'emergency_contact',
        'request_edit',
    ]
    list_editable = [
        'verified',
        'deliver_at_doorstep',
        'requested_verification',
        'request_edit',
    ]
    list_display_links = [
        'name',
        'mobile',
        'emergency_contact',
    ]
    list_filter = [
        'facility',
        'city',
        'verified',
        'deliver_at_doorstep',
        'requested_verification',
        'request_edit',
    ]
    search_fields = [
        'name',
        'note',
        'edit',
    ]


class HospitalAdmin(ImportExportModelAdmin):
    list_display = [
        'name',
        'mobile',
        'verified',
        'updated_at',
        'requested_verification',
        'emergency_contact',
        'request_edit',
    ]
    list_editable = [
        'verified',
        'requested_verification',
        'request_edit',
    ]
    list_display_links = [
        'name',
        'mobile',
        'emergency_contact',
    ]
    list_filter = [
        'verified',
        'requested_verification',
        'request_edit',
        'city',
    ]
    search_fields = [
        'name',
        'note',
        'edit',
    ]


class VolunteerAdmin(ImportExportModelAdmin):
    list_display = [
        'name',
        'mobile',
        'verified',
        'created_at',
        'alternate_mobile',
    ]
    list_editable = [
        'verified',
    ]
    list_display_links = [
        'name',
        'mobile',
        'created_at',
    ]
    list_filter = [
        'verified',
        'facilities',
        'city',
    ]
    search_fields = [
        'name',
        'mobile',
        'alternate_mobile',
        'note',
    ]


class ExperienceAdmin(ImportExportModelAdmin):
    list_display = [
        'service',
        'name',
        'mobile',
        'visible',
        'available',
        'created_at',
        'alternate_mobile',
    ]
    list_editable = [
        'visible',
    ]
    list_display_links = [
        'service',
        'name',
        'mobile',
    ]
    list_filter = [
        'service',
        'visible',
        'available',
    ]
    search_fields = [
        'name',
        'mobile',
        'alternate_mobile',
        'experience',
    ]


admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Experience, ExperienceAdmin)
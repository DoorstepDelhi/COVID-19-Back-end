from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import (
    State,
    City,
    Facility,
    Service,
    Hospital,
    Experience,
    Plasma,
    Request,
)

admin.site.site_header = "DoorstepDelhi.com - COVID-19 Resources"


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"


class CityAdmin(ImportExportModelAdmin):
    list_display = [
                    'id',
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
        'id',
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
        'id',
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
        'id',
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
        'id',
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
        'id',
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


class PlasmaAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'city',
        'blood_group',
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
        'city',
        'blood_group',
        'name',
        'mobile',
        'emergency_contact',
    ]
    list_filter = [
        'city',
        'blood_group',
        'verified',
        'requested_verification',
        'request_edit',
    ]
    search_fields = [
        'name',
        'mobile',
        'alternate_mobile',
        'note',
    ]


class RequestAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'city',
        'facility',
        'name',
        'mobile',
        'created_at',
        'fulfilled',
        'urgent',
        'volunteer_working',
    ]
    list_editable = [
        'fulfilled',
        'urgent',
        'volunteer_working',
    ]
    list_display_links = [
        'city',
        'facility',
        'name',
        'mobile',
    ]
    list_filter = [
        'city',
        'facility',
        'fulfilled',
        'urgent',
    ]
    search_fields = [
        'city',
        'facility',
        'name',
        'mobile',
        'alternate_mobile',
        'note',
    ]


admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Plasma, PlasmaAdmin)
admin.site.register(Request, RequestAdmin)
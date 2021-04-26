from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    StateViewSet,
    CityViewSet,
    FacilityViewSet,
    ServiceViewSet,
    HospitalViewSet,
    VolunteerViewSet,
    ExperienceViewSet,
)

router = DefaultRouter()
router.register("states", StateViewSet, basename="state-detail")
router.register("cities", CityViewSet, basename="city-detail")
router.register("facilities", FacilityViewSet, basename="facility-detail")
router.register("services", ServiceViewSet, basename="service-detail")
router.register("hospitals", HospitalViewSet, basename = "hospital-detail")
router.register("volunteers", VolunteerViewSet, basename="volunteer-detail")
router.register("experiences", ExperienceViewSet, basename="experience-detail")

urlpatterns = [
    path("", include(router.urls)),
]

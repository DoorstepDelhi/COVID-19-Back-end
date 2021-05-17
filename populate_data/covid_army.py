from core.models import State, City, Facility, Service

import requests
import urllib


def populate_cities():
    url = "https://api.covid.army/api/cities"
    response = requests.get(url)
    data = response.json()
    for city in data:
        city_qs = City.objects.filter(name=city['name'])
        if city_qs.exists():
            city_qs = city_qs[0]
            city_qs.hindi_name = city["hindiName"]
            city_qs.verified = True
            city_qs.save()
        else:
            city_created = City.objects.create(name=city["name"], hindi_name=city["hindiName"], verified=True)


def get_cities():
    url = "https://api.covid.army/api/cities"
    response = requests.get(url)
    data = response.json()
    return data


def populate_resources():
    url = "https://api.covid.army/api/resources"
    response = requests.get(url)
    data = response.json()
    for key, value in data.items():
        resource = Facility.objects.filter(name=key)
        if not resource.exists():
            resource_qs = Facility.objects.create(name=key)


def get_resources():
    url = "https://api.covid.army/api/resources"
    response = requests.get(url)
    data = response.json()
    return data.keys()


def populate_contacts():
    url = "https://api.covid.army/api/contacts/"
    response = requests.get(url)
    data = response.json()
    for contact in data:
        service = Service.objects.filter(mobile = contact["contact_no"])
        if not service.exists():
            city = City.objects.filter(name = contact["city"])[0]
            facility = Facility.objects.filter(name = contact["resource_type"])[0]
            service = Service.objects.create(
                name = contact['title'],
                mobile = contact['contact_no'],
                address = contact['address'],
            )
            service.city.add(city)
            service.facility.add(facility)
            service.save()


def covid_army():
    cities = get_cities()
    print("Got Cities")
    resources = get_resources()
    print(resources)
    populate_resources()
    for city in cities:
        city_qs = City.objects.filter(name=city['name'])[0]
        for resource in resources:
            resource_qs = Facility.objects.filter(name=resource)[0]

def populate():
    populate_cities()
    populate_resources()
    populate_contacts()

import os, django

from populate_data import covid_army

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid.settings")
django.setup()

covid_army.populate()
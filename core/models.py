from django.conf import settings
from django.db import models


class State(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "States"


class City(models.Model):
	state = models.ForeignKey("core.State", on_delete = models.CASCADE, null=True)
	name = models.CharField(max_length = 120)
	verified = models.BooleanField(default=False)
	hindi_name = models.CharField(max_length = 256, blank=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Cities"


class Facility(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField()
	deliver = models.BooleanField(default=False)

	def __str__(self):
		deliver = " (deliver)" if self.deliver else ""
		return self.name + deliver

	class Meta:
		verbose_name_plural = "Facilities"


class Service(models.Model):
	city = models.ManyToManyField("core.City")
	facility = models.ManyToManyField("core.Facility")
	name = models.CharField(max_length=256, blank=True, null=True)
	contact_person = models.CharField(max_length = 150, blank=True, null=True)
	mobile = models.CharField(max_length = 15)
	alternate_mobile = models.CharField(max_length = 15, blank=True, null=True)
	address = models.TextField(null=True, blank=True)
	verified = models.BooleanField(default=True)
	note = models.TextField(null=True, blank=True)
	lat = models.FloatField(null=True, blank=True)
	long = models.FloatField(null=True, blank=True)
	deliver_at_doorstep = models.BooleanField(default=False)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	requested_verification = models.BooleanField(default=False)
	emergency_contact = models.CharField(max_length=50, null=True, blank=True)
	opening_time = models.TimeField(null=True, blank=True)
	closing_time = models.TimeField(null=True, blank=True)
	request_edit = models.BooleanField(default=False)
	edit = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.name) + "-(" + str(self.mobile) + ")"


class Hospital(models.Model):
	city = models.ManyToManyField("core.City")
	name = models.CharField(max_length=500)
	mobile = models.CharField(max_length=15, unique=True)
	alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
	address = models.TextField(null=True, blank=True)
	verified = models.BooleanField(default=True)
	lat = models.FloatField(null=True, blank=True)
	long = models.FloatField(null=True, blank=True)
	total_oxygen_beds = models.PositiveSmallIntegerField(null=True, blank=True)
	total_ventilators = models.PositiveSmallIntegerField(null=True, blank=True)
	total_icu = models.PositiveSmallIntegerField(null=True, blank=True)
	available_oxygen_beds = models.PositiveSmallIntegerField(null=True, blank=True)
	available_ventilators = models.PositiveSmallIntegerField(null=True, blank=True)
	available_icu = models.PositiveSmallIntegerField(null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	requested_verification = models.BooleanField(default=False)
	emergency_contact = models.CharField(max_length=50, null=True, blank=True)
	opening_time = models.TimeField(null=True, blank=True)
	closing_time = models.TimeField(null=True, blank=True)
	request_edit = models.BooleanField(default=False)
	edit = models.TextField(blank=True, null=True)
	note = models.TextField(null=True, blank=True)

	def __str__(self):
		return str(self.name) + "-(" + str(self.mobile) + ")"


class Volunteer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
	city = models.ManyToManyField("core.City")
	name = models.CharField(max_length=128)
	mobile = models.CharField(max_length=15, unique=True)
	alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
	facilities = models.ManyToManyField("core.Facility", null=True)
	available_from = models.TimeField(blank=True, null=True)
	available_till = models.TimeField(blank=True, null=True)
	verified = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	note = models.TextField(blank=True, null=True)

	def __str__(self):
		return str(self.name) + "-(" + str(self.mobile) + ")"

	class Meta:
		verbose_name_plural = "Volunteers"


class Experience(models.Model):
	service = models.ForeignKey("core.Service", on_delete=models.CASCADE)
	name = models.CharField(max_length=150)
	mobile = models.CharField(max_length=16, null=True, blank=True)
	alternate_mobile = models.CharField(max_length=16, blank=True, null=True)
	experience = models.TextField()
	experienced_on = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	available = models.BooleanField(default=True)
	visible = models.BooleanField(default=True)

	def __str__(self):
		return self.service + "by - " + self.name


class Plasma(models.Model):

	blood_group_choices = (
		("A+", "A+"),
		("A-", "A-"),
		("B+", "B+"),
		("B-", "B-"),
		("O+", "O+"),
		("O-", "O-"),
		("AB-", "AB-"),
		("AB+", "AB+"),
	)

	city = models.ForeignKey("core.City", on_delete = models.PROTECT)
	blood_group = models.CharField(max_length=3, choices = blood_group_choices)
	name = models.CharField(max_length=500)
	mobile = models.CharField(max_length=15, unique=True)
	alternate_mobile = models.CharField(max_length=15, blank=True, null=True)
	address = models.TextField(null=True, blank=True)
	verified = models.BooleanField(default=True)
	lat = models.FloatField(null=True, blank=True)
	long = models.FloatField(null=True, blank=True)
	updated_at = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add=True)
	requested_verification = models.BooleanField(default=False)
	emergency_contact = models.CharField(max_length=50, null=True, blank=True)
	request_edit = models.BooleanField(default=False)
	edit = models.TextField(blank=True, null=True)
	note = models.TextField(null=True, blank=True)

	def __str__(self):
		return str(self.city) + " - " + str(self.blood_group)


class Request(models.Model):
	city = models.ForeignKey("core.City", on_delete=models.CASCADE, null=True, blank=True)
	facility = models.ForeignKey("core.Facility", on_delete=models.CASCADE, null=True, blank=True)
	name = models.CharField(max_length=150)
	mobile = models.CharField(max_length=15)
	alternate_mobile = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	note = models.TextField(blank=True, null=True)
	fulfilled = models.BooleanField(default=False)
	fulfilled_on = models.DateTimeField(blank=True, null=True)
	urgent = models.BooleanField(default=False)
	volunteer_working = models.ForeignKey("core.Volunteer", on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return str(self.name) + "(" + str(self.mobile) + ")"

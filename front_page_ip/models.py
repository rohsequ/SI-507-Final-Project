from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=40)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name="s_country")
    name = models.CharField(max_length=40)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name="ci_country")
    state = models.ForeignKey(State, null=True, on_delete=models.CASCADE,related_name="ci_state")
    name = models.CharField(max_length=40)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class PersonLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,related_name="p_country")
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True,related_name="p_state")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,related_name="p_city")
    ip_address = models.GenericIPAddressField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    def __str__(self):
        return self.user.first_name

class LocationData(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,related_name="loc_country")
    state = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,related_name="loc_state")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True,related_name="loc_city")

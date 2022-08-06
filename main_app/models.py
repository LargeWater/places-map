import geocoder 
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoibGFyZ2V3YXRlciIsImEiOiJjbDZoOTAwZWkweWNjM2JvYThnbm03YjMzIn0.r11MoNzvczr0RUCDmi9brQ'


class Place(models.Model):
  address = models.TextField()
  lat = models.FloatField(blank=True, null=True)
  lng = models.FloatField(blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    g = geocoder.mapbox(self.address, key=mapbox_access_token)
    g = g.latlng
    self.lat = g[0]
    self.lng = g[1]
    return super(Place, self).save(*args, **kwargs)
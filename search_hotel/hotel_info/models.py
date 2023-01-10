from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Hotel_info(models.Model):
  img = models.FileField(upload_to="media")
  hotelname = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  longitude = models.FloatField(max_length=255)
  latitude = models.FloatField(max_length=255)
  geopoint = models.PointField()


  def __str__(self):
    return f"{self.hotelname} {self.address} {self.description} {self.longitude} {self.latitude} {self.geopoint}"

  def save(self):
    self.geopoint = Point(self.longitude, self.latitude)
    super(Hotel_info, self).save()
    
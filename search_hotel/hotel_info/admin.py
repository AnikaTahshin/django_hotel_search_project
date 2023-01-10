from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hotel_info




# Register your models here.

# class Hotel_info_Admin(admin.ModelAdmin):
#     list_display = ("hotelname", "address", "description","longitude","latitude","geopoint")


class Hotel_info_Admin(OSMGeoAdmin):
    list_display = ("hotelname", "address", "description","longitude","latitude","geopoint")



admin.site.register(Hotel_info,Hotel_info_Admin)




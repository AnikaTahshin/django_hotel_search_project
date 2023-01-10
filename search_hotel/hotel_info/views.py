# from django import template
from django.http import HttpResponse
from django.template import loader
from django.contrib.gis.geos import Point, GEOSGeometry
from django.shortcuts import render
from .models import Hotel_info
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from hotel_info import models
from django.contrib.gis.db.models.functions import Distance


def info(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def location(request):
  long = request.GET.get('lon'),
  lat = request.GET.get('lat'),
  rad = request.GET.get('radius'),
  #breakpoint()
 
  inputPoint = Point(float(long[0]), float(lat[0]), srid=4326)

  # input = str(inputPoint)
  
 

  data = Hotel_info.objects.annotate(distance=Distance('geopoint',inputPoint)).order_by('distance').filter(distance__lte=D(km=int(rad[0])))
  
  context = {'data':data}
  # return HttpResponse(template.render())
  return render(request,'getdata.html',context)
  




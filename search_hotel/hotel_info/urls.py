from django.urls import path
from . import views

urlpatterns = [
    path('hotel_info/', views.info),
    path('hotel_info/getdata.html',views.location)
]
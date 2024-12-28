from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('vehiculo/add', views.add_vehicle, name='add_vehicle'),
               path('vehiculo/list', views.list_vehicles, name='list_vehicles'),
               ]

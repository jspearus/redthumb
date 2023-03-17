from django.shortcuts import render
from rest_framework import viewsets, filters
import threading

from rest_framework import viewsets          # add this
from .serializers import PlantRecordSerializer, ChannelDataSerializer, PlantDbSerializer      # add this

from .client import startClient
from .models import PlantRecord, ChannelData, PlantDb





inputThead = threading.Thread(target=startClient, args=())
inputThead.setDaemon(True)
inputThead.start()

# Create your views here.
def red(request):
    return render(request, 'index.html', {
        'name': 'Jeff'
    })

class PlantRecordView(viewsets.ModelViewSet):       # add this
    serializer_class = PlantRecordSerializer          # add this
    queryset = PlantRecord.objects.all()            # add this
    search_fields = ['name', 'plant_type', 'moisture_lvl', 'humidity_lvl', 
                     'water_added', 'time']
    filter_backends = (filters.SearchFilter,)

    
class ChannelDataView(viewsets.ModelViewSet):       # add this
    serializer_class = ChannelDataSerializer          # add this
    queryset = ChannelData.objects.all()              # add this
    search_fields = ['ch_id', 'ch_number', 'plant_type', 'plant_name',
                     'last_water_added']
    filter_backends = (filters.SearchFilter,)

    
class PlantDbView(viewsets.ModelViewSet):       # add this
    serializer_class = PlantDbSerializer          # add this
    queryset = PlantDb.objects.all()              # add this
    search_fields = ['plant_type', 'max_moisture_lvl', 'min_moisture_lvl', 'max_temperature_lvl', 'min_temperature_lvl',
                     'max_humidity_lvl', 'min_humidity_lvl', 'min_light_lvl', 'max_light_lvl',
                     'daylight_time', 'amount_water', 'hours_between_watering']
    filter_backends = (filters.SearchFilter,)

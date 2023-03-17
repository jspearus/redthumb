from rest_framework import serializers
from .models import PlantRecord, ChannelData, PlantDb


class PlantRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantRecord
        fields = ('id', 'name', 'plant_type', 'moisture_lvl',
                  'temperature_lvl', 'humidity_lvl', 'light_lvl',
                  'water_added', 'time',)
        
class ChannelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelData
        fields = ('ch_id', 'ch_number', 'plant_type', 'plant_name', 'last_water_added')
        
class PlantDbSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantDb
        fields = ('id', 'plant_type', 'max_moisture_lvl', 'min_moisture_lvl', 'max_temperature_lvl',
                  'min_temperature_lvl', 'max_humidity_lvl', 'min_humidity_lvl',
                  'min_light_lvl', 'max_light_lvl', 'daylight_time',
                  'amount_water', 'hours_between_watering')
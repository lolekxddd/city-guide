from rest_framework import serializers
from attraction.models import Attraction
from django.conf import settings


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = [
            'pk',
            'name',
            'description',
            'city',
            'rate',
            'price',
            'category',
            'latitude',
            'longitude',
            'start_h',
            'end_h',      
        ]
    def validate_name(self,value):
        qs = Attraction.objects.filter(name=value)
        if qs.exists():
            raise serializers.ValidationError("Nazwa musi być unikalna")
        return value
from rest_framework import serializers
from models import Targets, Missions, Details, Planets

class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = ('id', 'name', 'slug', 'body_type', 'image_url', 'characteristics', 'curiosities', 'sim_related')

class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = ('id', 'target', 'era', 'name', 'codename', 'hashed', 'image_url', 'launch_dates')

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('id', 'mission', 'detail_type', 'header', 'body', 'date', 'image_link')

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ('target', 'discover', 'rings', 'light', 'mass', 'diameter', 'density', 'gravity', 'l_day', 'l_year', 'eccent', 'distance', 'perihelion', 'aphelion', 'inclination', 'active', 'atmosphere')
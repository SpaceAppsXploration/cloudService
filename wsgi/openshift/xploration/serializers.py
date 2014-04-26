from rest_framework import serializers
from models import Targets, Missions, Details

class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = ('id', 'name', 'body_type', 'image_url', 'characteristics', 'curiousities', 'sim_related')

class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = ('id', 'target', 'era', 'name', 'codename', 'hashed', 'image_url', 'launch_date')

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('id', 'mission', 'detail_type', 'header', 'body', 'date', 'image_link')

class PlanetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planets
        fields = ('id', 'discover', 'rings', 'light', 'mass', 'diameter', 'density', 'gravity', 'l_day', 'l_year', 'eccent', 'distance', 'perihelion', 'aphelion', 'inclination', 'active', 'atmosphere')
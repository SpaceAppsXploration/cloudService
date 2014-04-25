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
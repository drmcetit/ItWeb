from rest_framework import serializers

from .models import carouselModel,AssosiationMembersModel,PlacementModel

class carouselSerializer(serializers.ModelSerializer):

    class Meta:
        model=carouselModel
        fields=[
            'Titile',
            'Description',
            'ButtonText',
            'Image',
            'Display'
        ]

class AssositationSerializer(serializers.ModelSerializer):

    class Meta:
        model=AssosiationMembersModel
        fields=[
            'Name',
            'Desigination',
            'Year',
            'ProfilePic'
        ]

class PlacmentSerializer(serializers.ModelSerializer):

    class Meta:
        model=PlacementModel
        fields=[
            'Name',
            'Batch',
            'Placed',
            'Desigination',
            'LPA',
            'StartUp',
            'Company',
            'ProfilePic'
        ]
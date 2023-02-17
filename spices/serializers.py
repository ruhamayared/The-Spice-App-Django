from .models import Spice
from django.contrib.auth.models import User, Group
from rest_framework import serializers

#SpiceSerializer
class SpiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        #The model it will serialize
        model = Spice
        #The fields that should be included in the serialized output
        fields = ['id', 'name', 'description', 'image']
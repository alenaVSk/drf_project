from rest_framework import serializers
from .models import DeliciousWay
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class DeliciousWaySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = DeliciousWay
        fields = ("__all__")


from rest_framework import serializers
from .models import DeliciousWay


class DeliciousWaySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliciousWay
        fields = ('title', 'cat_id')

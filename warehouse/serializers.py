from rest_framework import serializers

from .models import StockRoom


class StockRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRoom
        fields = ['id', 'name']

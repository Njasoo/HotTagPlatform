from rest_framework import serializers
from .models import HotItem


class HotItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotItem
        fields = "__all__"

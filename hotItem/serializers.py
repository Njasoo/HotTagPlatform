from rest_framework import serializers
from .models import HotItem
from django.utils.timezone import localtime


class HotItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotItem
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.crawl_time:
            data["crawl_time"] = localtime(instance.crawl_time).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        return data

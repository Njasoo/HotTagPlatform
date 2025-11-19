from rest_framework.serializers import ModelSerializer
from .models import WordCloud


class WordCloudSerializer(ModelSerializer):
    class Mata:
        model = WordCloud
        fields = "__all__"

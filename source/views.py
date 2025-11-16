from rest_framework.generics import ListAPIView
from .models import Source
from .serializers import SourceSerializer


class SourceListView(ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

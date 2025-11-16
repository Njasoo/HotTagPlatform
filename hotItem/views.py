from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HotItem
from .serializers import HotItemSerializer


class HotItemView(APIView):
    def get(self, request):
        source = request.GET.get("source", None)
        if not source:
            queryset = HotItem.objects.all()
            serializer = HotItemSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = HotItem.objects.filter(source=source)
        queryset = queryset.order_by("rank")
        serializer = HotItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

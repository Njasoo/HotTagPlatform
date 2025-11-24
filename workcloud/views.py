from rest_framework.views import APIView
from .models import WordCloud
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class WordCloudAPIView(APIView):
    @method_decorator(cache_page(60 * 60))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        source = request.query_params.get("source")
        url = WordCloud.objects.get(
            source__value=source
        ).url  # 实际上source关联的还是对象，要这样获取列名
        return Response({"url": url}, status=status.HTTP_200_OK)

from .models import HotItem
from .serializers import HotItemSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class HotItemPagination(PageNumberPagination):
    page_size = 10  # 默认每页10条记录
    page_size_query_param = "page_size"  # 前端参数命名, .e.g ?page_size=114


class HotItemView(ListAPIView):
    serializer_class = HotItemSerializer
    pagination_class = HotItemPagination

    @method_decorator(cache_page(60 * 60))  # 存一个小时
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = HotItem.objects.all()
        source = self.request.GET.get("source", None)
        category = self.request.query_params.get("category", None)
        if source:
            queryset = queryset.filter(source=source)  # 不赋值是不会修改queryset的
        if category:
            queryset = queryset.filter(category=category)
        queryset = queryset.order_by("rank")
        return queryset

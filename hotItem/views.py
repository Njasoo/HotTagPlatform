from .models import HotItem
from .serializers import HotItemSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination


class HotItemPagination(PageNumberPagination):
    page_size = 10  # 默认每页10条记录
    page_size_query_param = "page_size"  # 前端参数命名, .e.g ?page_size=114


class HotItemView(ListAPIView):
    serializer_class = HotItemSerializer
    pagination_class = HotItemPagination

    def get_queryset(self):
        queryset = HotItem.objects.all()
        source = self.request.GET.get("source", None)
        if source:
            queryset = queryset.filter(source=source).order_by(
                "rank"
            )  # 不赋值是不会修改queryset的
        return queryset

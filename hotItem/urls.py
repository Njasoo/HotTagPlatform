from django.urls import path
from .views import HotItemView

urlpatterns = [
    path("hot/", HotItemView.as_view(), name="hot-view"),
]

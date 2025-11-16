from django.urls import path
from .views import SourceListView

urlpatterns = [
    path("source/", SourceListView.as_view(), name="source-list"),
]

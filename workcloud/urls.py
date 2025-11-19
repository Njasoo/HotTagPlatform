from .views import WordCloudAPIView
from django.urls import path

urlpatterns = [
    path("wordcloud/", WordCloudAPIView.as_view(), name="wordcloud"),
]

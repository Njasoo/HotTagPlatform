from django.db import models
from source.models import Source


class HotItem(models.Model):
    title = models.CharField(max_length=255)  # 最长就只能存255个字符
    source = models.ForeignKey(Source, to_field="value", on_delete=models.CASCADE)
    rank = models.IntegerField()
    url = models.URLField(max_length=500)
    category = models.CharField(max_length=255, blank=True, null=True)
    crawl_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

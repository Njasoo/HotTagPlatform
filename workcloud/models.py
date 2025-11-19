from django.db import models
from source.models import Source


class WordCloud(models.Model):
    url = models.TextField()
    source = models.ForeignKey(Source, to_field="value", on_delete=models.CASCADE)

    def __str__(self):
        return self.url

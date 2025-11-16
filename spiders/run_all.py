from weibo_spider import fetch_weibo_hot
from zhihu_spider import fetch_zhihu_hot
from bilibili_spider import fetch_bilibili_hot
import os
import django
import sys

current_file_path = os.path.abspath(__file__)
BASE_URL = os.path.dirname(os.path.dirname(current_file_path))
sys.path.append(BASE_URL)
# assert False
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from hotItem.models import HotItem

if __name__ == "__main__":
    res_weibo = fetch_weibo_hot()
    res_zhihu = fetch_zhihu_hot()
    res_bilibili = fetch_bilibili_hot()
    res = res_weibo + res_bilibili + res_zhihu
    HotItem.objects.all().delete()
    for x in res:
        HotItem.objects.create(
            title=x["title"], rank=x["rank"], source_id=x["source"], url=x["url"]
        )
    queryset = HotItem.objects.all()
    print(queryset)

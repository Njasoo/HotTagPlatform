from transformers import pipeline
import os
import sys
import django

currentPath = os.path.abspath(__file__)
BASE_URL = os.path.dirname(os.path.dirname(currentPath))
sys.path.append(BASE_URL)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from hotItem.models import HotItem


classifier = pipeline(
    "text-classification", model="uer/roberta-base-finetuned-chinanews-chinese"
)

en2zh = {
    "mainland China politics": "中国大陆政治",
    "Hong Kong - Macau politics": "港澳政治",
    "International news": "国际新闻",
    "financial news": "财经新闻",
    "culture": "文化",
    "entertainment": "娱乐",
    "sports": "体育",
}

# while True:
#     title = input("\n请输入一个标题（输入q退出）：\n>")
#     if title.lower() == "q":
#         break
#     result = classifier(title)[0]
#     print("\n分类结果")
#     print(f"类别: {en2zh[result['label']]} 置信度: {result['score']:.4f}")


def run():
    queryset = HotItem.objects.all()
    hoitems_to_update = []
    for hotitem in queryset:
        result = classifier(hotitem.title)[0]
        result = en2zh[result["label"]]
        hotitem.category = result
        hoitems_to_update.append(hotitem)
    HotItem.objects.bulk_update(
        hoitems_to_update, ["category"]
    )  # 第二个参数也是指定要更新的列，这样就不会更新整个对象


if __name__ == "__main__":
    run()

import jieba
import jieba.posseg
import os
import sys
import django
import requests
from collections import Counter

currentPath = os.path.abspath(__file__)
BASE_URL = os.path.dirname(os.path.dirname(currentPath))
sys.path.append(BASE_URL)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from hotItem.models import HotItem
from splitwords.wordcloud_work import get_wordcloud
from workcloud.models import WordCloud

stop_words_urls = [
    "https://raw.githubusercontent.com/goto456/stopwords/refs/heads/master/baidu_stopwords.txt",
    "https://raw.githubusercontent.com/goto456/stopwords/refs/heads/master/cn_stopwords.txt",
    "https://raw.githubusercontent.com/goto456/stopwords/refs/heads/master/hit_stopwords.txt",
    "https://raw.githubusercontent.com/goto456/stopwords/refs/heads/master/scu_stopwords.txt",
]

stopwords = set()

for stop_words_url in stop_words_urls:
    response = requests.get(stop_words_url)
    stopwords.update(response.text.splitlines())


def get_words(source):
    titles = HotItem.objects.filter(source=source).values_list("title", flat=True)
    words = []
    for title in titles:
        words.extend(jieba.posseg.lcut(title))  # lcut直接返回数组
    words = [
        word.word
        for word in words
        if word.word not in stopwords
        and word.word.strip()
        and word.flag.startswith("n")
    ]  # 只保留名词
    return words


def get_top_words(words, num):
    counter = Counter(words)
    top_words = counter.most_common(num)
    return top_words


def run(source):
    words = get_words(source)
    top_words = get_top_words(words, 100)
    url = get_wordcloud(top_words)
    WordCloud.objects.create(url=url, source_id=source)

    # current_dir = os.path.dirname(currentPath)
    # test_path = os.path.join(current_dir, "test.txt")
    # with open(test_path, "w", encoding="utf-8") as f:
    #     for x in stopwords:
    #         f.write(x + "\n")


if __name__ == "__main__":
    WordCloud.objects.all().delete()
    source_list = ["weibo", "bilibili", "zhihu"]
    for source in source_list:
        run(source)

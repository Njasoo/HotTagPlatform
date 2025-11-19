import requests as rq
import json
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Cookie": "SUB=_2AkMeSm12f8NxqwFRmv0WzGPmb49-zgjEieKoFpytJRMxHRl-yT9yqlUjtRB6NcpDmXB8v7jCDdUOANFsLEoZJwuDT4Wu; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5Ip-3.Qjwa_aD0wH30D.qZ; _s_tentry=passport.weibo.com; Apache=8441114877984.956.1763107391573; SINAGLOBAL=8441114877984.956.1763107391573; ULV=1763107391574:1:1:1:8441114877984.956.1763107391573:",
}


def is_in_rank(x):
    # 拿纯文本字符串，html也会直接变成字符串
    text = x.get_text(strip=True)
    return text.isdigit()


def fetch_weibo_hot():
    url = "https://s.weibo.com/top/summary?cate=realtimehot"
    res = rq.get(url, headers=headers)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text, "lxml")
    # print(soup)
    # local_dir = os.path.dirname(os.path.abspath(__file__))
    # test_path = os.path.join(local_dir, "test.txt")
    # with open(test_path, "w", encoding="utf-8") as f:
    #     f.write(soup.prettify())
    a_tags = soup.select("td.td-02 a")
    td_01_s = soup.select("td.td-01")
    assert len(td_01_s) == len(a_tags)
    cnt = 0
    res = []
    for i in range(len(a_tags)):
        a_tag = a_tags[i]
        td_01 = td_01_s[i]
        if not is_in_rank(td_01):
            continue
        link = "https://s.weibo.com" + a_tag.get("href")
        cnt += 1
        new_obj = {"title": a_tag.string, "rank": cnt, "source": "weibo", "url": link}
        res.append(new_obj)
    return res


if __name__ == "__main__":
    res = fetch_weibo_hot()
    print(res)

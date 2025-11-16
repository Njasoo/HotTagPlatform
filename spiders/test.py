import requests


def fetch_zhihu_hot():
    # 1️⃣ 填写你的知乎登录 Cookie
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        ),
        "Cookie": "d_c0=ACCSP_n7sBmPTqAfstHfRNmJThQjim4dRo4=|1734153943; edu_user_uuid=edu-v1|6c290b97-4ab3-4097-a423-022ac3319e21; _xsrf=nRn9AuXVUNK9SgL0D6d0lEUDam5bboA8; _zap=c10fdbd7-e0d4-4376-81cc-b9627e0a449a; q_c1=507330dc373845c9968dd9a5efd1b275|1747292054000|1747292054000; __zse_ck=004_bwynY81gz0CZsxedzz8XvH37FR8OesgFZAsaqPtsFOR0=6FZT9cJU/Y7jCNeKVjnj2dO42Y1YonxmlgMIc7PHYiKLIC7grJTxOKQLVr9bmBAmi3LhnOMleppWIlGmJxz-ZGkyPQPWxOW70EHmu0RNyKRQCItL4+1XpRvUEuFFgqvBrTTUcg6jBF6G+o8NOsz95CUnGYy8kkWN2Gvuq9id29AXHI2lX3ULrdNLkRajlLJk9SnR9K1vM58Q8jSRREwE; z_c0=2|1:0|10:1763016789|4:z_c0|92:Mi4xTWs4LUJnQUFBQUFBSUpJXy1mdXdHU1lBQUFCZ0FsVk5KeUg0YVFEd0tOczdqZDA5Z3ZXcmU3UWExcjcweUh1alFR|402add9d33be5562ed797d2d0cc139ee131107c45032977d3cee63a2d9f4bf4d; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1762317093,1762835739,1763016788,1763093619; HMACCOUNT=1AD53EA21F9AB7AC; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1763103156; BEC=f7bc18b707cd87fca0d61511d015686f; SESSIONID=jeatsiguy2QWSp29CGRbPYzi8Hvb0D9HYLeD94qQfk8; JOID=WlEUB0nlwGs7gu14MekL_nql9rYsjq0PSfuFF0GW8zJp15dLAFscfl6J5HUyPIyEsausAIOoDBv2rmiFnfxM6KY=; osd=V1kWAEPoyGk8iOBwM-4B83Kn8bwhhq8IQ_aNFUac_jpr0J1GCFkbdFOB5nI4MYSGtqGhCIGvBhb-rG-PkPRO76w=",  # 请替换成你自己的 Cookie
    }

    # 2️⃣ API 地址
    url = "https://www.zhihu.com/api/v4/feed/topstory/hot-lists/total?limit=50"

    # 3️⃣ 发送请求
    res = requests.get(url, headers=headers)

    # 4️⃣ 检查状态
    if res.status_code != 200:
        print(f"请求失败，状态码：{res.status_code}")
        print(res.text)
        return

    # 5️⃣ 解析 JSON 数据
    data = res.json()
    hot_list = data.get("data", [])

    if not hot_list:
        print("没有拿到热榜数据，可能 Cookie 失效")
        return

    # 6️⃣ 打印热榜标题和链接
    for idx, item in enumerate(hot_list, 1):
        target = item.get("target", {})
        title = target.get("title", "无标题")
        link = target.get("link", "无链接")
        print(f"{idx}. {title} -> {link}")


if __name__ == "__main__":
    fetch_zhihu_hot()

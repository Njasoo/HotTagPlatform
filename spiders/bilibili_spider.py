import requests as rq
import json
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Cookie": "buvid_fp_plain=undefined; DedeUserID=13239429; DedeUserID__ckMd5=37bf1fca732a4e57; enable_web_push=DISABLE; is-2022-channel=1; LIVE_BUVID=AUTO9117368678669572; rpdid=|(u|kk~~|Juk0J'u~J)~RJ)|m; enable_feed_channel=ENABLE; fingerprint=9e77e4393f9892df96e63ea7ed7a0259; buvid_fp=9e77e4393f9892df96e63ea7ed7a0259; buvid3=5B93C263-35DF-E31E-D4B8-E9037EADBCCC11919infoc; b_nut=1748070611; _uuid=2F66BBA6-31B3-FA84-F9EA-6BDF1107CE16F13823infoc; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; buvid4=04B0E06E-37BC-14EA-6650-B964FE9120E282882-022052412-sJpF461V+BQZFwDq/Nbdlw%3D%3D; hit-dyn-v2=1; CURRENT_BLACKGAP=0; ogv_device_support_hdr=0; home_feed_column=4; CURRENT_QUALITY=112; PVID=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjMyODMzNTIsImlhdCI6MTc2MzAyNDA5MiwicGx0IjotMX0.9gEq1SWLxOM7vGGuXLqBaMpKH3syg4jUUBnYP4Wjvk4; bili_ticket_expires=1763283292; browser_resolution=1396-632; SESSDATA=8efba8c1%2C1778597974%2C509e7%2Ab1CjAm87n9xUw5XNroNx0AjaWgnsgdZkO9UQJdnaKUzLVWg_aUZT1bnCTD6OH6BHde0C4SVjhvX0NsUnR1WW9UZTFYWjh2c3dKVW5NdzZySkZ3OHVGcEhaUkFSM1Z2XzQ1Y3k5RmZkaF9rWlVVV2N4Znk5NExCX3Itdmozbnl4TnNxU2RvSWk2aFNBIIEC; bili_jct=3d9191b7dfff198b8848a64a0ed8b485; sid=5e6bwsd9; bp_t_offset_13239429=1134994062005239808; CURRENT_FNVAL=4048; b_lsid=16D310F3E_19A811B801D",
}


def fetch_bilibili_hot():
    url = "https://s.search.bilibili.com/main/hotword"
    res = rq.get(url, headers=headers)
    res.encoding = "utf-8"
    res = res.json()
    # local_dir = os.path.dirname(os.path.abspath(__file__))
    # test_path = os.path.join(local_dir, "test.json")
    # with open(test_path, "w", encoding="utf-8") as f:
    #     json.dump(res, f, ensure_ascii=False)
    data = res.get("list", {})
    res = []
    now_rank = 1
    for x in data:
        title = x.get("show_name", {})
        url = f"https://www.bilibili.com/search?keyword={title}"
        new_obj = {"title": title, "source": "bilibili", "rank": now_rank, "url": url}
        res.append(new_obj)
        now_rank += 1
    return res


if __name__ == "__main__":
    res = fetch_bilibili_hot()
    print(res)

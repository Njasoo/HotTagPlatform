import requests as rq
import json
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Cookie": 'BIDUPSID=AF6A69DC50A78E7187D9E6838B850F11; PSTM=1734154456; MAWEBCUID=web_JyQAhIsKfrxOWHzcGIRpaFzqviSFdPXbDEnSJAbScZAemxWxGA; IS_NEW_USER=5bb88ae85c323f68d18f9a2a; TIEBAUID=aba520f5b6ef53a110682444; BDUSS=haUVQxdThrcUhmYnFXdmNINXNyWWdEb35HM35GY21Ia2Jsa09jOWFnYkRXVlZvSVFBQUFBJCQAAAAAAAAAAAEAAAAqWWdZzfXmguWpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPMLWjDzC1oSG; BDUSS_BFESS=haUVQxdThrcUhmYnFXdmNINXNyWWdEb35HM35GY21Ia2Jsa09jOWFnYkRXVlZvSVFBQUFBJCQAAAAAAAAAAAEAAAAqWWdZzfXmguWpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMPMLWjDzC1oSG; BAIDUID=6CE6E51A30820105B936C83E324A7FC1:SL=0:NR=10:FG=1; BAIDUID_BFESS=6CE6E51A30820105B936C83E324A7FC1:SL=0:NR=10:FG=1; BAIDU_WISE_UID=wapp_1756995605334_380; __bid_n=19961599cc828323f8e50a; H_WISE_SIDS_BFESS=60272_62325_63144_63324_63947_64363_64438_64450_64460_64557_64600_64650_64670_64709_64722_64741_64743_64739_64824_64815_64870_64882_64841_64905_64927_64957_64934_64979; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=3; delPer=0; STOKEN=75d6bd22e426594f5f802ac0f4cd485f6ecb24bed6e4e7ef48dc480210f65c35; Hm_lvt_292b2e1608b0823c1cb6beef7243ef34=1762402485,1762861001,1763480017; USER_JUMP=-1; HMACCOUNT=1AD53EA21F9AB7AC; st_key_id=17; wise_device=0; 1499945258_FRSVideoUploadTip=1; video_bubble1499945258=1; H_PS_PSSID=60272_63144_65894_65361_65988_66125_66149_66215_66211_66245_66362_66257_66393_66394_66453_66461_66470_66482_66516_66529_66553_66584_66579_66593; H_WISE_SIDS=60272_63144_65894_65361_65988_66125_66149_66215_66211_66245_66362_66257_66393_66394_66453_66461_66470_66482_66516_66529_66553_66584_66579_66593; arialoadData=false; ZFY=EgNDpCAUsKUsFzvstys3x:BPkXBrldEwPQq2KCc8ftWg:C; RT="z=1&dm=baidu.com&si=06a4df6f-324a-4035-b7b5-7504c33c2363&ss=mie6unwf&sl=3&tt=26d&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2wn&ul=3yr&hd=3yu"; TIEBA_SID=H4sIAAAAAAAAAzO0NDUzNok3BgC9jWcoCAAAAA; XFI=8c932410-c9cc-11f0-adcc-d92d6724497d; XFCS=A1A90648E9AF1E56647DA6A99D7054D8B6415BA71E751AFF07888B608325504E; XFT=BWz96BEvEFDD/JdHA02c4emCVYcyYKvLRBFuwNvSmUI=; BA_HECTOR=ak2k2l258g0004a12h81ak200k258l1kialjg25; ariaappid=c890648bf4dd00d05eb9751dd0548c30; ariauseGraymode=false; Hm_lpvt_292b2e1608b0823c1cb6beef7243ef34=1764054640; ab_sr=1.0.1_ZWRiOWNjZGQ2MjBmZDBiNjlhNjUxN2ZlMGYwMmZjN2Q2M2M3NmZlN2NlYWEzODlhMThkYjEyNjBlNDJmMzE4ZGJmYjhkNDQxOTRkOGVkOTUzNzlmZmJmZmY3ZmI3MTk4OWUzNTU1MzQxNGFlZWQwMzNkMWNiZThlNmFiOTEzNmEzY2E1NmIyOTQyNmNjMmU5YjIwNDZmYjEwZTM1NTVkMDM2MmFjNmMwZTBhZDI2ZTJmYWQzYjFlOTFhMGIzYWU1; st_data=ecd0afb271e45049b9106e23e29dfb92e845ae7c7c1cb53dcfee0c602d06ca48790201ce75186accae670af55a4a3eaf270409bcb1bc952b28aff2d393f804a0f56402ed55797012479fb3052f67192c3d725705d96cb10dc2d06fe1201050d8c25ed2b394f1ba15ca8fdb64f134de9af3ef96b64fdba4bcd075a0bbf2bb66b22a4201846e7bc454972f3c4c92c51b9a; st_sign=a09071e0',
}


def fetch_tieba_hot():
    url = "https://tieba.baidu.com/hottopic/browse/topicList"
    res = rq.get(url, headers=headers)
    res.encoding = "utf-8"
    res = res.json()
    # local_dir = os.path.dirname(os.path.abspath(__file__))
    # test_path = os.path.join(local_dir, "test.json")
    # with open(test_path, "w", encoding="utf-8") as f:
    #     json.dump(res, f, ensure_ascii=False)
    topic_list = res["data"]["bang_topic"]["topic_list"]
    rest = []
    for topic in topic_list:
        title = topic["topic_name"]
        link = topic["topic_url"]
        rank = topic["idx_num"]
        rest.append(
            {
                "title": title,
                "rank": rank,
                "url": link,
                "source": "tieba",
            }
        )
    return rest


if __name__ == "__main__":
    res = fetch_tieba_hot()
    print(res)

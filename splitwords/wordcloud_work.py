from wordcloud import WordCloud
import matplotlib

matplotlib.use("Agg")  # 使用无GUI的后端
import matplotlib.pyplot as plt
import os
import numpy as np
import io
import base64

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
font_file_path = os.path.join(current_dir, "fonts/MSYH.TTC")


def get_circle_mask(size=500):
    x, y = np.ogrid[:size, :size]
    center = size / 2
    radius = size / 2
    mask = (x - center) ** 2 + (y - center) ** 2 > radius**2
    mask = mask.astype(int) * 255  # 转成白色背景（255=白）
    return mask


def get_wordcloud(top_words):
    freq_dict = dict(top_words)

    circle_mask = get_circle_mask(1000)

    wc = WordCloud(
        font_path=font_file_path,
        width=1000,
        height=1000,
        background_color=None,
        mode="RGBA",
        mask=circle_mask,
        colormap="tab10",
    )

    wc.generate_from_frequencies(freq_dict)  # 用词频字典生成词云

    buffer = io.BytesIO()
    plt.figure(figsize=(10, 10))  # 不写这行代码图会很糊

    # 显示
    plt.imshow(wc)  # 这里是把图像画出来
    # ❗确保背景是透明的
    plt.gca().set_facecolor("none")
    plt.axis("off")
    plt.axis("off")  # 关闭坐标轴
    plt.savefig(
        buffer,
        format="svg",
        bbox_inches="tight",
        pad_inches=0,
        transparent=True,  # svg矢量图
    )  # save到内存里面
    plt.close()

    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode(
        "utf-8"
    )  # 先是编码成base64字符串，然后decode成普通字符串
    return f"data:image/svg+xml;base64,{img_base64}"

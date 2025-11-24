## 项目简介

HotTagPlatform 后端服务，为前端和移动端提供 **实时热榜数据 API**。  
支持多来源、多分类热榜查询，并结合缓存优化访问性能。

在线网站（需要 VPN 或境外访问）: https://htpf.vercel.app

主要功能：

- 热榜数据增删改查
- 支持 `source` / `category` 筛选
- 分页接口，方便前端展示
- 缓存支持（Django cache + Render Key-Value / Redis）
- 生成热榜词云
- 可部署到 Render 或其他云平台

## 技术栈

- Python 3.14
- Django / Django REST Framework
- PostgreSQL（生产） / SQLite（开发）
- Redis / Render Key-Value（缓存）
- Render（生产部署）

## 安装与运行（开发环境）

```bash
git clone https://github.com/Njasoo/HotTagPlatform.git
cd HotTagPlatform
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

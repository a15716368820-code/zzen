# 个人博客 (Django)

功能：分类/标签/评论/搜索/RSS + 主题切换（卡片/极简/暗黑）。

## 本地运行
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

访问：`http://127.0.0.1:8000`

## Docker 运行
```bash
docker compose up -d --build
```

## 管理后台
`/admin` 进入后台发布文章、配置站点主题/标题。

## RSS
`/rss/`

## 搜索
首页顶部搜索框。

## 主题
后台 SiteSetting 里切换：cards/minimal/dark。

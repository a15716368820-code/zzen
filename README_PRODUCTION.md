# zzen 生产部署指南

## 环境准备

复制环境变量模板：

```bash
cp .env.example .env
```

填写：

- SECRET_KEY
- 数据库密码
- 域名

## Docker 部署

构建并启动：

```bash
docker compose up -d --build
```

执行迁移：

```bash
docker compose exec web python manage.py migrate
```

收集静态文件：

```bash
docker compose exec web python manage.py collectstatic --noinput
```

## 检查安全配置

```bash
docker compose exec web python manage.py check --deploy
```

## 常用维护

查看日志：

```bash
docker compose logs -f web
```

备份 PostgreSQL：

```bash
docker compose exec db pg_dump -U blog blog > backup.sql
```

# ZZEN AI OS

Open source AI Agent Operating System foundation.

当前仓库包含 Django 基础平台，并逐步演进为 AI Agent 平台。

## Roadmap

- Agent Runtime
- Multi-Agent Workflow
- Knowledge Base / RAG
- Model Router
- Enterprise Workspace
- Plugin Architecture

## Local Run

```bash
python -m venv .venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Docker

```bash
docker compose up -d --build
```

## License

MIT

FROM python:3.11-slim

WORKDIR /app

COPY app/pyproject.toml pyproject.toml
COPY app/requirements.lock requirements.lock
COPY app/requirements-dev.lock requirements-dev.lock
COPY app/README.md README.md

RUN pip install --no-cache-dir -r requirements.lock || pip install --no-cache-dir -r requirements-dev.lock

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
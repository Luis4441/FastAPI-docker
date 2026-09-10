FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOST=127.0.0.1

WORKDIR /app

# Copy requirements first to leverage layer caching. If a lock file is provided
# the image will prefer it; otherwise it falls back to requirements.txt.
COPY requirements.txt ./
COPY requirements.lock ./

# Install dependencies: prefer `requirements.lock` when present, else use
# `requirements.txt`. This conditional avoids failing the build when a lock
# file is not provided yet.
RUN if [ -f requirements.lock ]; then \
            pip install --no-cache-dir --only-binary=:all: -r requirements.lock; \
        else \
            pip install --no-cache-dir --only-binary=:all: -r requirements.txt; \
        fi

COPY main.py ./
COPY swagger.html ./

EXPOSE 8000

# Create an unprivileged user and run the app as that user
RUN addgroup --system app && adduser --system --ingroup app appuser \
    && chown -R appuser:app /app

USER appuser

CMD ["sh", "-c", "python -m uvicorn main:app --host ${HOST} --port 8000"]

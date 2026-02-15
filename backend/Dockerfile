FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv (default installer for this project)
ADD --chmod=755 https://astral.sh/uv/install.sh /tmp/uv-install.sh
RUN /tmp/uv-install.sh && rm /tmp/uv-install.sh
ENV PATH="/root/.local/bin:$PATH"

COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "opc.wsgi:application"]

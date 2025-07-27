FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY ../../requirements/base.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN mkdir -p src/{print_data,logs,config,database, models}

COPY src/print_data/ src/print_data/
COPY src/logs/ src/logs/
COPY src/config/ src/config/
COPY src/database/ src/database/
COPY src/models/ src/models/

RUN useradd --create-home --shell /bin/bash app && \
    chown -R app:app /app
USER app

CMD ["python", "src/print_data/main.py"]
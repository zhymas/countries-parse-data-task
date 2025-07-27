FROM python:3.11-slim

WORKDIR /app

COPY ../../requirements/base.txt .

RUN pip install -r base.txt

COPY . .

CMD ["python", "src/get_data/main.py"]
FROM python:3.13-slim
RUN pip install --upgrade pip
COPY requirements.txt .

WORKDIR .
COPY . .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8080", "main:py"]

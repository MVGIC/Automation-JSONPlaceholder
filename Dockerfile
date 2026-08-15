FROM python:3.11-slim
WORKDIR /app

COPY /requirements.txt .
COPY /test_docker/test_print.py .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["pytest", "-sv", "test_print.py"]

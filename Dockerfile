FROM mcr.microsoft.com/playwright/python:v1.43.1-jammy

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]

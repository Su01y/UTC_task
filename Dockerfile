FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc libpq-dev

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "-c"]
CMD ["uvicorn app.app:app --host 0.0.0.0 --port 8000"]
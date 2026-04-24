FROM python:3.11-slim

WORKDIR /app

# زيادة الـ timeout لتجنب انقطاع الشبكة
ENV PIP_DEFAULT_TIMEOUT=300
ENV PIP_RETRIES=5

COPY requirements.txt .

RUN pip install --no-cache-dir --timeout=300 -r requirements.txt

COPY src/api/ ./src/api/
COPY mlflow/satisfaction_model.pkl ./mlflow/

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
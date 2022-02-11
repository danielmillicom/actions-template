FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

EXPOSE 8080

CMD ["uvicorn", "app.business.app:app", "--host", "0.0.0.0", "--port", "8080"]
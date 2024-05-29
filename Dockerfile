
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY warehouse/manage.py /app/
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

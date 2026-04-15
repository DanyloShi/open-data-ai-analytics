FROM python:3.12-slim
WORKDIR /app
COPY visualization/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY common /app/common
COPY visualization/app.py /app/visualization/app.py
CMD ["python", "visualization/app.py"]

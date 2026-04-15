FROM python:3.12-slim
WORKDIR /app
COPY data_load/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY common /app/common
COPY data_load/app.py /app/data_load/app.py
CMD ["python", "data_load/app.py"]

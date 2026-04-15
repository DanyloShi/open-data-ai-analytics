FROM python:3.12-slim
WORKDIR /app
COPY data_research/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY common /app/common
COPY data_research/app.py /app/data_research/app.py
CMD ["python", "data_research/app.py"]

FROM python:3.12-slim
WORKDIR /app
COPY data_quality_analysis/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY common /app/common
COPY data_quality_analysis/app.py /app/data_quality_analysis/app.py
CMD ["python", "data_quality_analysis/app.py"]

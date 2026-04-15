FROM python:3.12-slim
WORKDIR /app
COPY web/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY common /app/common
COPY web/app.py /app/web/app.py
COPY web/templates /app/web/templates
COPY web/static /app/web/static
EXPOSE 8080
CMD ["python", "web/app.py"]

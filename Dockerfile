FROM python:3.9.0-alpine

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./src/main.py .
CMD ["python", "./main.py"]




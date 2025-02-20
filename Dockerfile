FROM python:3.11-slim

WORKDIR /

RUN pip install --no-cache-dir -r requirements.txt
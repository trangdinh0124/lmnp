# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /lmnp
COPY requirements.txt ./
COPY . ./
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python manage.py migrate


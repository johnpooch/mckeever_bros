FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
COPY dev_requirements.txt /code/

RUN pip install -r requirements.txt
RUN pip install -r dev_requirements.txt
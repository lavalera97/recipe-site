FROM python:3.9
MAINTAINER Semenov Valery

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip -r requirements.txt

COPY . /code/
FROM python:3.10

WORKDIR /app

RUN apt update && apt -qy upgrade

COPY requirements /app/requirements

RUN pip install -r requirements/dev.txt

COPY . /app/

ENV PYTHONPATH /app/app


WORKDIR /app/

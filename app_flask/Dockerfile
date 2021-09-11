FROM python:3.8.7-slim-buster

COPY ./requirements.txt /project/requirements.txt
WORKDIR /project

RUN apt update \
  && apt install -y gcc
RUN pip install -r requirements.txt

COPY . /project/

ENTRYPOINT [ "uwsgi", "--ini", "/project/uwsgi.ini" ]
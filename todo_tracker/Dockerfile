FROM python:3.8-slim

#RUN apt-get install \
#    jpeg-dev \
#    zlib-dev \
#    sqlite3

RUN mkdir /todo_tracker
WORKDIR /todo_tracker

COPY requirements.txt /todo_tracker/
RUN pip install -r requirements.txt

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

COPY . /todo_tracker/
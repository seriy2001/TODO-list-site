FROM python:3.8-slim

RUN mkdir /app
WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED 1
ENV PORT=8000

RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

EXPOSE 8000
# CMD gunicorn todo_tracker.wsgi:application --bind 0.0.0.0:$PORT

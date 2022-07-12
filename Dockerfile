# syntax=docker/dockerfile:1
FROM python:3.8.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update
RUN apt install docker.io -y
RUN docker --version
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN curl -sSL https://get.docker.com/ | sh
COPY . /code/
ENTRYPOINT nohup dockerd >/dev/null 2>&1 & sleep 10 && python manage.py runserver 0.0.0.0:8000




FROM python:3.7-slim-buster

EXPOSE 8000

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV DOCKER
ENV DJANGO_SU_NAME admin
ENV DJANGO_SU_EMAIL dan@fake.com
## Bad practice. Only for development ##
ENV DJANGO_SU_PASSWORD admin 

RUN apt-get update && apt-get upgrade -y

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

CMD ["bash", "entrypoint.sh"]
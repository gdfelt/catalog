FROM python:3.7-alpine

EXPOSE 8000

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy project
COPY . /usr/src/app/

CMD ["gunicorn", "catalog_backend.wsgi:application", "--name", "catalog", "--bind", "0.0.0.0:8000"]
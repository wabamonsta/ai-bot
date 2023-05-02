FROM python:3.6.1-alpine
ARG PROJECT_NAME
RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
RUN mkdir /var/www/html/${PROJECT_NAME}
WORKDIR /var/www/html/${PROJECT_NAME}
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
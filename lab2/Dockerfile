#DOCKERFILE DO database_container1000 ZROBIONEGO Z IMAGE'U database_psql:v2


# FROM postgres:11.18-alpine

# ENV POSTGRES_USER postgres123
# ENV POSTGRES_PASSWORD pass123
# ENV POSTGRES_DB mydatabase123

# COPY init.sql /docker-entrypoint-initdb.d/

# EXPOSE 5432






#DOCKERFILE DO "SCRAPY_APP" ZROBIONEGO Z IMAGE'U scrapy_app:v1 ; trochę go zmodyfikowałem w stosunku do instrukcji, by działał bardziej customowo

FROM python:3.8-slim-buster

WORKDIR /job_scraper

# Zaktualizuj system i zainstaluj GCC oraz inne narzędzia niezbędne do kompilacji
RUN apt-get update && apt-get install -y gcc build-essential

COPY job_scraper /job_scraper

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "scrapy", "crawl", "nazwa_spidera" ]






# #DOCKERFILE DO database_container1000 ZROBIONEGO Z IMAGE'U jupter/base-notebook:v1

# FROM jupyter/base-notebook

# WORKDIR /job_scraper

# COPY job_scraper /job_scraper

# RUN pip install -r requirements.txt

FROM postgres:11.18-alpine

ENV POSTGRES_USER postgres123
ENV POSTGRES_PASSWORD pass123
ENV POSTGRES_DB mydatabase123

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5432
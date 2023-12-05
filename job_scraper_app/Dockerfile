#DOCKERFILE DO "SCRAPY_APP" ZROBIONEGO Z IMAGE'U scrapy_app:v1 ; trochę go zmodyfikowałem w stosunku do instrukcji, by działał bardziej customowo

FROM python:3.8-slim-buster

WORKDIR /job_scraper_app

# Zaktualizuj system i zainstaluj GCC oraz inne narzędzia niezbędne do kompilacji
RUN apt-get update && apt-get install -y gcc build-essential

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "scrapy", "crawl", "new_offers_spider" ]
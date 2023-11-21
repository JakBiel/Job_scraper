import scrapy
import psycopg2
import json
import datetime
from scrapy import signals
from bs4 import BeautifulSoup
from pydispatch import dispatcher


import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s')

class NazwaSpideraSpider(scrapy.Spider):
    name = 'nazwa_spidera'
    allowed_domains = ['https://nofluffjobs.com','nofluffjobs.com']
    base_url = 'https://nofluffjobs.com'
    start_urls = ['https://nofluffjobs.com/pl/Python?gclid=Cj0KCQjwiIOmBhDjARIsAP6YhSV2DGRihkNNThMktarn4I_6FTXFx85xJBRx2HS64Xh3NlE6xWvHk3EaAnFlEALw_wcB&page=1']

    page = 1  # Numer strony startowej

    iterator_wiadomosci = 0
    iterator_sublinkow = 0

    def parse_subpage(self, response):

        offer_item = {
            "offer_link": response.url,
            "offer_name": response.xpath('//*[@id="posting-header"]/div[1]/div/h1/text()').get(),
            "company": response.xpath('/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/common-posting-header/div/div/a/text()').get(),
            "main_location": response.css("span.tw-overflow-hidden.tw-overflow-ellipsis.tw-whitespace-nowrap::text").get(),
            "other_location": response.css("div.tw-flex.tw-items-center.tw-w-full.ng-star-inserted::text").get(),
            "salary": response.xpath('/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[2]/common-apply-box/div/div[1]/common-posting-salaries-list/div/h4/text()').get(),
            "salary_type": response.xpath("/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[2]/common-apply-box/div/div[1]/common-posting-salaries-list/div/div/span/text()").get(),
            "main_requirements_description": response.css('section[data-cy-section="JobOffer_Requirements"] ::text').getall(),
            "main_offer_description": response.css('section[data-cy-section="JobOffer_Project"] ::text').getall(),
            "your_responsibilities": response.css('section[data-cy-section="JobOffer_DailyTasks"] ::text').getall(),
            "offer_details": response.css('section#posting-specs ul li.detail::text').getall(),            
            "equipment_supplied": response.css('section#posting-equipment li.benefit-wrapper span.mobile-text::text').getall(),
            "methodology": response.css('section#posting-environment ul li span.with-value::text').getall(),
            "perks_in_the_office": response.css('section.purple ul li span::text').getall(),
            "benefits": response.css('section.success ul li span::text').getall(),
            "company_foundation_year": response.css('li:contains("Founded in:") p::text').get(),
            "company_size": response.css('li:contains("Company size:") p::text').get(),
            "company_head_office_place": response.css('li:contains("Main location:") p::text').get(),
            "date_of_scrapping": datetime.datetime.now().isoformat(),         
            "when_published_relatively": response.css("div.posting-time-row.ng-star-inserted::text").get(),
            "categories": response.xpath('/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-posting-details/div/common-main-loader/main/article/div[1]/common-posting-content-wrapper/div[1]/section[1]/ul/li[1]/div/aside/div/a/text()').getall(),
            "skills_maturity": response.css("span.mr-10.font-weight-medium.ng-star-inserted::text").get(),
            "tags_mandatory": response.xpath('//section[h2="Must have"]/ul/li/span/text()').getall(),
            "tags_nice_to_have": response.xpath('//section[h2="Nice to have"]/ul/li/span/text()').getall()
        }
        yield offer_item

    def parse(self, response):

        #UWAGA: Ten kod przechodzi też przez linki regionalne, ale z drugiej strony w innej części projektu jest filtracja podobnych ofert jeśli chodzi o zarobki
        subpage_links = response.xpath('/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-postings-search/div/div/common-main-loader/nfj-search-results/nfj-postings-list/div[3]//a[1]/@href').getall()

        
        #ten kod tylko przystosowuje wybrane, nieprzygotowane hiperłącza do odczytu przez parse_subpage(), bo nie wszystkie zaczynają  się od "/"
        for indeks, element in enumerate(subpage_links):
            if not element.startswith("/"):
                subpage_links[indeks] = "/" + element
        
       
        yield from response.follow_all(subpage_links, callback=self.parse_subpage)
            

        #PONIZEJ MODUL SLUZACY DO CRAWLOWANIA MIEDZY KOLEJNYMI STRONAMI (NIE MYLIC Z CRAWLOWANIEM PO SUBSTRONACH STRONY):
        
        #next_page = response.xpath("/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-postings-search/div/common-main-loader/nfj-search-results/  div/nfj-pagination/ul/li[last()]/a[1]/@href") #tutaj implementujemy, w jaki sposób chcemy zrobić crawling, by scrapować na nowej stronce. Tu - crawling poprzez guziczek ze stronki
        next_page = response.xpath("/html/body/nfj-root/nfj-layout/nfj-main-content/div/nfj-postings-search/div/div/common-main-loader/nfj-search-results/div/nfj-pagination/ul/li[last()]/a[1]/@href")

        logging.info(f"Aktualna postać: {next_page}")

        if next_page.get():
            logging.info(f"Następna strona: {next_page}")
            yield response.follow(f'{self.base_url}{next_page.get()}', callback=self.parse)




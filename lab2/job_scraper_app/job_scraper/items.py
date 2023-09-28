# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
  
import scrapy
from scrapy.item import Item, Field

class JobScraperItem(scrapy.Item):

    offer_link = Field()
    offer_name = Field()
    company = Field()
    main_location = Field()
    other_location = Field()
    salary = Field()
    salary_type = Field()
    main_requirements_description = Field()
    main_offer_description = Field()
    your_responsibilities = Field()
    offer_details = Field()
    equipment_supplied = Field()
    methodology = Field()
    perks_in_the_office = Field()
    benefits = Field()
    company_info_Founded_in = Field()
    company_info_Company_size = Field()
    company_info_Main_location = Field()
    date_of_scrapping = Field()
    when_published_relatively = Field()
    categories = Field()
    skills_maturity = Field()
    tags_mandatory = Field()
    tags_nice_to_have = Field()

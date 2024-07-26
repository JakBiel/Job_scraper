# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2

class PostgreSQLPipeline:
    
    def __init__(self, postgresql_settings):
        self.postgresql_settings = postgresql_settings

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        postgresql_settings = settings.get('POSTGRESQL_SETTINGS')
        return cls(postgresql_settings)

    def open_spider(self, spider):
        self.connection = psycopg2.connect(**self.postgresql_settings)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def is_duplicate(self, item):
        query = """SELECT COUNT(*) FROM new_offers WHERE 
                   offer_name = %s AND 
                   salary = %s AND 
                   salary_type = %s AND 
                   company = %s"""
        self.cursor.execute(query, (item['offer_name'], item['salary'], item['salary_type'], item['company']))
        count = self.cursor.fetchone()[0]
        return count > 0
    
    def validation_of_item(self, item):
        
        keys_to_process = [
            'offer_link', 'offer_name', 'company', 'main_location', 'other_location', 
            'salary', 'salary_type', 'main_requirements_description', 'main_offer_description', 
            'your_responsibilities', 'offer_details', 'equipment_supplied', 'methodology', 
            'perks_in_the_office', 'benefits', 'company_foundation_year', 'company_size', 
            'company_head_office_place', 'date_of_scrapping', 'when_published_relatively', 
            'categories', 'skills_maturity', 'tags_mandatory', 'tags_nice_to_have'
            ]
        
        for key in keys_to_process:
            if item.get(key):
                if isinstance(item[key], list):
                    item[key] = ', '.join([tag.strip() for tag in item[key] if tag.strip()])
                    if not item[key]:
                        item[key] = '<None>'
                else:
                    item[key] = item[key].strip('{}').strip()
                    if not item[key] or item[key] == '{}':
                        item[key] = '<None>'
                if key == 'main_requirements_description' and item[key] != '<None>':
                    item[key] = item[key].replace("Requirements description, ", "").strip()
                if key == 'main_offer_description' and item[key] != '<None>':
                    item[key] = item[key].replace("Offer description, ", "").strip()
                if key == 'your_responsibilities' and item[key] != '<None>':
                    item[key] = item[key].replace("Your responsibilities, ", "").strip()
                if key == 'when_published_relatively' and item[key] != '<None>':
                    item[key] = item[key].replace("This offer was published", "").strip()
            else:
                item[key] = '<None>'
            return item

    def process_item(self, item, spider):
        
        insert_query = "INSERT INTO new_offers (offer_link,offer_name,company,main_location,other_location,salary,salary_type,main_requirements_description,main_offer_description,your_responsibilities,offer_details,equipment_supplied,methodology,perks_in_the_office,benefits,company_foundation_year,company_size,company_head_office_place,date_of_scrapping,when_published_relatively,categories,skills_maturity,tags_mandatory,tags_nice_to_have) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        self.validation_of_item(item)

        if self.is_duplicate(item):
            spider.logger.info(f"Item {item['offer_name']} from {item['company']} is duplicated. Skipping...")
            return item  # zwróć item, ale nie dodawaj go do bazy, bo to duplikat

        data = (item['offer_link'], item['offer_name'], item['company'], item['main_location'], item['other_location'], item['salary'], item['salary_type'], item['main_requirements_description'], item['main_offer_description'], item['your_responsibilities'], item['offer_details'], item['equipment_supplied'], item['methodology'], item['perks_in_the_office'], item['benefits'], item['company_foundation_year'], item['company_size'], item['company_head_office_place'], item['date_of_scrapping'], item['when_published_relatively'], item['categories'], item['skills_maturity'], item['tags_mandatory'], item['tags_nice_to_have'])

        self.cursor.execute(insert_query, data)
        self.connection.commit()
        return item

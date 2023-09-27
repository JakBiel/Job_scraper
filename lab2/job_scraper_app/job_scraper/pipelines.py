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

    def process_item(self, item, spider):
        # Przetwarzaj pola item przed wstawieniem ich do bazy danych

        # item['category'] = item['category'].strip('{}').strip()
        # item['language'] = item['language'].strip('{}').strip()

        # item['offer_link'] = item['offer_link'].strip('{}').strip()
        # item['offer_name'] = item['offer_name'].strip('{}').strip()
        # item['company']
        # item['main_location']
        # item['other_location']
        # item['salary']
        # item['salary_type']
        # item['main_requirements_description']
        # item['main_offer_description']
        # item['your_responsibilities']
        # item['offer_details']
        # item['equipment_supplied']
        # item['methodology']
        # item['perks_in_the_office']
        # item['benefits']
        # item['company_info_Founded_in']
        # item['company_info_Company_size']
        # item['company_info_Main_location']
        # item['date_of_scrapping']
        # item['when_published_relatively']
        # item['categories']
        # item['skills_maturity']
        # item['tags_mandatory']
        # item['tags_nice_to_have']

        # if item['offer_link']:
        #     if isinstance(item['offer_link'], list):
        #         item['offer_link'] = ', '.join(item['offer_link'])
        #     item['offer_link'] = item['offer_link'].strip('{}').strip()

        # if item['offer_name']:
        #     if isinstance(item['offer_name'], list):
        #         item['offer_name'] = ', '.join(item['offer_name'])
        #     item['offer_name'] = item['offer_name'].strip('{}').strip()

        # if item['company']:
        #     if isinstance(item['company'], list):
        #         item['company'] = ', '.join(item['company'])
        #     item['company'] = item['company'].strip('{}').strip()

        # if item['main_location']:
        #     if isinstance(item['main_location'], list):
        #         item['main_location'] = ', '.join(item['main_location'])
        #     item['main_location'] = item['main_location'].strip('{}').strip()

        # if item['other_location']:
        #     if isinstance(item['other_location'], list):
        #         item['other_location'] = ', '.join(item['other_location'])
        #     item['other_location'] = item['other_location'].strip('{}').strip()

        # if item['salary']:
        #     if isinstance(item['salary'], list):
        #         item['salary'] = ', '.join(item['salary'])
        #     item['salary'] = item['salary'].strip('{}').strip()

        # if item['salary_type']:
        #     if isinstance(item['salary_type'], list):
        #         item['salary_type'] = ', '.join(item['salary_type'])
        #     item['salary_type'] = item['salary_type'].strip('{}').strip()

        # if item['main_requirements_description']:
        #     if isinstance(item['main_requirements_description'], list):
        #         item['main_requirements_description'] = ', '.join(item['main_requirements_description'])
        #     item['main_requirements_description'] = item['main_requirements_description'].strip('{}').strip()

        # if item['main_offer_description']:
        #     if isinstance(item['main_offer_description'], list):
        #         item['main_offer_description'] = ', '.join(item['main_offer_description'])
        #     item['main_offer_description'] = item['main_offer_description'].strip('{}').strip()

        # if item['your_responsibilities']:
        #     if isinstance(item['your_responsibilities'], list):
        #         item['your_responsibilities'] = ', '.join(item['your_responsibilities'])
        #     item['your_responsibilities'] = item['your_responsibilities'].strip('{}').strip()

        # if item['offer_details']:
        #     if isinstance(item['offer_details'], list):
        #         item['offer_details'] = ', '.join(item['offer_details'])
        #     item['offer_details'] = item['offer_details'].strip('{}').strip()

        # if item['equipment_supplied']:
        #     if isinstance(item['equipment_supplied'], list):
        #         item['equipment_supplied'] = ', '.join(item['equipment_supplied'])
        #     item['equipment_supplied'] = item['equipment_supplied'].strip('{}').strip()

        # if item['methodology']:
        #     if isinstance(item['methodology'], list):
        #         item['methodology'] = ', '.join(item['methodology'])
        #     item['methodology'] = item['methodology'].strip('{}').strip()

        # if item['perks_in_the_office']:
        #     if isinstance(item['perks_in_the_office'], list):
        #         item['perks_in_the_office'] = ', '.join(item['perks_in_the_office'])
        #     item['perks_in_the_office'] = item['perks_in_the_office'].strip('{}').strip()

        # if item['benefits']:
        #     if isinstance(item['benefits'], list):
        #         item['benefits'] = ', '.join(item['benefits'])
        #     item['benefits'] = item['benefits'].strip('{}').strip()

        # if item['company_info_Founded_in']:
        #     if isinstance(item['company_info_Founded_in'], list):
        #         item['company_info_Founded_in'] = ', '.join(item['company_info_Founded_in'])
        #     item['company_info_Founded_in'] = item['company_info_Founded_in'].strip('{}').strip()

        # if item['company_info_Company_size']:
        #     if isinstance(item['company_info_Company_size'], list):
        #         item['company_info_Company_size'] = ', '.join(item['company_info_Company_size'])
        #     item['company_info_Company_size'] = item['company_info_Company_size'].strip('{}').strip()

        # if item['company_info_Main_location']:
        #     if isinstance(item['company_info_Main_location'], list):
        #         item['company_info_Main_location'] = ', '.join(item['company_info_Main_location'])
        #     item['company_info_Main_location'] = item['company_info_Main_location'].strip('{}').strip()

        # if item['date_of_scrapping']:
        #     if isinstance(item['date_of_scrapping'], list):
        #         item['date_of_scrapping'] = ', '.join(item['date_of_scrapping'])
        #     item['date_of_scrapping'] = item['date_of_scrapping'].strip('{}').strip()

        # if item['when_published_relatively']:
        #     if isinstance(item['when_published_relatively'], list):
        #         item['when_published_relatively'] = ', '.join(item['when_published_relatively'])
        #     item['when_published_relatively'] = item['when_published_relatively'].strip('{}').strip()

        # if item['categories']:
        #     if isinstance(item['categories'], list):
        #         item['categories'] = ', '.join(item['categories'])
        #     item['categories'] = item['categories'].strip('{}').strip()

        # if item['skills_maturity']:
        #     if isinstance(item['skills_maturity'], list):
        #         item['skills_maturity'] = ', '.join(item['skills_maturity'])
        #     item['skills_maturity'] = item['skills_maturity'].strip('{}').strip()

        # if item['tags_mandatory']:
        #     if isinstance(item['tags_mandatory'], list):
        #         item['tags_mandatory'] = ', '.join(item['tags_mandatory'])
        #     item['tags_mandatory'] = item['tags_mandatory'].strip('{}').strip()

        # if item['tags_nice_to_have']:
        #     if isinstance(item['tags_nice_to_have'], list):
        #         item['tags_nice_to_have'] = ', '.join(item['tags_nice_to_have'])
        #     item['tags_nice_to_have'] = item['tags_nice_to_have'].strip('{}').strip()





        # if item['offer_link']:
        #     if isinstance(item['offer_link'], list):
        #         item['offer_link'] = ', '.join([tag.strip() for tag in item['offer_link']])
        #     else:
        #         item['offer_link'] = item['offer_link'].strip('{}').strip()

        # if item['offer_name']:
        #             if isinstance(item['offer_name'], list):
        #                 item['offer_name'] = ', '.join([tag.strip() for tag in item['offer_name']])
        #             else:
        #                 item['offer_name'] = item['offer_name'].strip('{}').strip()

        # if item['company']:
        #             if isinstance(item['company'], list):
        #                 item['company'] = ', '.join([tag.strip() for tag in item['company']])
        #             else:
        #                 item['company'] = item['company'].strip('{}').strip()

        # if item['main_location']:
        #             if isinstance(item['main_location'], list):
        #                 item['main_location'] = ', '.join([tag.strip() for tag in item['main_location']])
        #             else:
        #                 item['main_location'] = item['main_location'].strip('{}').strip()

        # if item['other_location']:
        #             if isinstance(item['other_location'], list):
        #                 item['other_location'] = ', '.join([tag.strip() for tag in item['other_location']])
        #             else:
        #                 item['other_location'] = item['other_location'].strip('{}').strip()

        # if item['salary']:
        #             if isinstance(item['salary'], list):
        #                 item['salary'] = ', '.join([tag.strip() for tag in item['salary']])
        #             else:
        #                 item['salary'] = item['salary'].strip('{}').strip()

        # if item['salary_type']:
        #             if isinstance(item['salary_type'], list):
        #                 item['salary_type'] = ', '.join([tag.strip() for tag in item['salary_type']])
        #             else:
        #                 item['salary_type'] = item['salary_type'].strip('{}').strip()

        # if item['main_requirements_description']:
        #             if isinstance(item['main_requirements_description'], list):
        #                 item['main_requirements_description'] = ', '.join([tag.strip() for tag in item['main_requirements_description']])
        #             else:
        #                 item['main_requirements_description'] = item['main_requirements_description'].strip('{}').strip()

        # if item['main_offer_description']:
        #             if isinstance(item['main_offer_description'], list):
        #                 item['main_offer_description'] = ', '.join([tag.strip() for tag in item['main_offer_description']])
        #             else:
        #                 item['main_offer_description'] = item['main_offer_description'].strip('{}').strip()

        # if item['your_responsibilities']:
        #             if isinstance(item['your_responsibilities'], list):
        #                 item['your_responsibilities'] = ', '.join([tag.strip() for tag in item['your_responsibilities']])
        #             else:
        #                 item['your_responsibilities'] = item['your_responsibilities'].strip('{}').strip()

        # if item['offer_details']:
        #             if isinstance(item['offer_details'], list):
        #                 item['offer_details'] = ', '.join([tag.strip() for tag in item['offer_details']])
        #             else:
        #                 item['offer_details'] = item['offer_details'].strip('{}').strip()

        # if item['equipment_supplied']:
        #             if isinstance(item['equipment_supplied'], list):
        #                 item['equipment_supplied'] = ', '.join([tag.strip() for tag in item['equipment_supplied']])
        #             else:
        #                 item['equipment_supplied'] = item['equipment_supplied'].strip('{}').strip()

        # if item['methodology']:
        #             if isinstance(item['methodology'], list):
        #                 item['methodology'] = ', '.join([tag.strip() for tag in item['methodology']])
        #             else:
        #                 item['methodology'] = item['methodology'].strip('{}').strip()

        # if item['perks_in_the_office']:
        #             if isinstance(item['perks_in_the_office'], list):
        #                 item['perks_in_the_office'] = ', '.join([tag.strip() for tag in item['perks_in_the_office']])
        #             else:
        #                 item['perks_in_the_office'] = item['perks_in_the_office'].strip('{}').strip()

        # if item['benefits']:
        #             if isinstance(item['benefits'], list):
        #                 item['benefits'] = ', '.join([tag.strip() for tag in item['benefits']])
        #             else:
        #                 item['benefits'] = item['benefits'].strip('{}').strip()

        # if item['company_info_Founded_in']:
        #             if isinstance(item['company_info_Founded_in'], list):
        #                 item['company_info_Founded_in'] = ', '.join([tag.strip() for tag in item['company_info_Founded_in']])
        #             else:
        #                 item['company_info_Founded_in'] = item['company_info_Founded_in'].strip('{}').strip()

        # if item['company_info_Company_size']:
        #             if isinstance(item['company_info_Company_size'], list):
        #                 item['company_info_Company_size'] = ', '.join([tag.strip() for tag in item['company_info_Company_size']])
        #             else:
        #                 item['company_info_Company_size'] = item['company_info_Company_size'].strip('{}').strip()

        # if item['company_info_Main_location']:
        #             if isinstance(item['company_info_Main_location'], list):
        #                 item['company_info_Main_location'] = ', '.join([tag.strip() for tag in item['company_info_Main_location']])
        #             else:
        #                 item['company_info_Main_location'] = item['company_info_Main_location'].strip('{}').strip()

        # if item['date_of_scrapping']:
        #             if isinstance(item['date_of_scrapping'], list):
        #                 item['date_of_scrapping'] = ', '.join([tag.strip() for tag in item['date_of_scrapping']])
        #             else:
        #                 item['date_of_scrapping'] = item['date_of_scrapping'].strip('{}').strip()

        # if item['when_published_relatively']:
        #             if isinstance(item['when_published_relatively'], list):
        #                 item['when_published_relatively'] = ', '.join([tag.strip() for tag in item['when_published_relatively']])
        #             else:
        #                 item['when_published_relatively'] = item['when_published_relatively'].strip('{}').strip()

        # if item['categories']:
        #             if isinstance(item['categories'], list):
        #                 item['categories'] = ', '.join([tag.strip() for tag in item['categories']])
        #             else:
        #                 item['categories'] = item['categories'].strip('{}').strip()

        # if item['skills_maturity']:
        #             if isinstance(item['skills_maturity'], list):
        #                 item['skills_maturity'] = ', '.join([tag.strip() for tag in item['skills_maturity']])
        #             else:
        #                 item['skills_maturity'] = item['skills_maturity'].strip('{}').strip()

        # if item['tags_mandatory']:
        #             if isinstance(item['tags_mandatory'], list):
        #                 item['tags_mandatory'] = ', '.join([tag.strip() for tag in item['tags_mandatory']])
        #             else:
        #                 item['tags_mandatory'] = item['tags_mandatory'].strip('{}').strip()

        # if item['tags_nice_to_have']:
        #             if isinstance(item['tags_nice_to_have'], list):
        #                 item['tags_nice_to_have'] = ', '.join([tag.strip() for tag in item['tags_nice_to_have']])
        #             else:
        #                 item['tags_nice_to_have'] = item['tags_nice_to_have'].strip('{}').strip()



        def process_item(key, item):
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


        keys_to_process = [
            'offer_link', 'offer_name', 'company', 'main_location', 'other_location', 
            'salary', 'salary_type', 'main_requirements_description', 'main_offer_description', 
            'your_responsibilities', 'offer_details', 'equipment_supplied', 'methodology', 
            'perks_in_the_office', 'benefits', 'company_info_Founded_in', 'company_info_Company_size', 
            'company_info_Main_location', 'date_of_scrapping', 'when_published_relatively', 
            'categories', 'skills_maturity', 'tags_mandatory', 'tags_nice_to_have'
            ]

        for key in keys_to_process:
            item = process_item(key, item)



        insert_query = "INSERT INTO new_offers (offer_link,offer_name,company,main_location,other_location,salary,salary_type,main_requirements_description,main_offer_description,your_responsibilities,offer_details,equipment_supplied,methodology,perks_in_the_office,benefits,company_info_Founded_in,company_info_Company_size,company_info_Main_location,date_of_scrapping,when_published_relatively,categories,skills_maturity,tags_mandatory,tags_nice_to_have) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        data = (item['offer_link'], item['offer_name'], item['company'], item['main_location'], item['other_location'], item['salary'], item['salary_type'], item['main_requirements_description'], item['main_offer_description'], item['your_responsibilities'], item['offer_details'], item['equipment_supplied'], item['methodology'], item['perks_in_the_office'], item['benefits'], item['company_info_Founded_in'], item['company_info_Company_size'], item['company_info_Main_location'], item['date_of_scrapping'], item['when_published_relatively'], item['categories'], item['skills_maturity'], item['tags_mandatory'], item['tags_nice_to_have'])

        self.cursor.execute(insert_query, data)
        self.connection.commit()
        return item
    





    # if item['tags_mandatory']:
    #         if isinstance(item['tags_mandatory'], list):
    #             item['tags_mandatory'] = ', '.join([tag.strip() for tag in item['tags_mandatory']])
    #         else:
    #             item['tags_mandatory'] = item['tags_mandatory'].strip('{}').strip()
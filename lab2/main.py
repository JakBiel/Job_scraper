import requests
from bs4 import BeautifulSoup


#adres_url = "https://nofluffjobs.com/pl/Data?criteria=keyword%3Dengineer&page=1"
#page = requests.get(adres_url)

#print(page)

#print(page.content)

# parsedOffer = {
#         'title': title,
#         'companyName': companyName,
#         'experienceLevels': experienceLevels,
#         'languages': json.dumps(languages),
#         'requirements': json.dumps(requirements),
#         'additionalRequirements': json.dumps(additionalRequirements),
#         'description': description,
#         'salaries': json.dumps(salaries),
#         'locations': json.dumps(locations)
#     }

# url2 = "https://nofluffjobs.com/pl/job/data-engineer-silent-eight-remote-orqukozb" #oferta wygasla, daję nowy link

# url2 = "https://nofluffjobs.com/pl/job/big-data-developer-flaire-remote-gwoylvzr"

url3 = "https://pl.jooble.org/SearchResult?ukw=data%20engineer"

page2 = requests.get(url3)

#print(page2)

#print(page2.content)

parsedOffer = {
        'title': 0,
        'companyName': 0,
        'experienceLevels': 0,
        'languages': 0,
        'requirements': 0,
        'additionalRequirements': 0,
        'description': 0,
        'salaries': 0,
        'locations': 0
    }

soup = BeautifulSoup(page2.content, 'html.parser')

#print(soup.prettify())

# title = soup.find('h1').text
# for link in soup.find_all('h1'):
#     print(link.text)


# for tag in soup.find_all(text=" Big Data Developer "):
#     print(tag.name)
#     print("\n")
#     for tag1 in tag.parents:
#         print(tag1.name)
#     print("\n\n\n\n")


# for tag in soup.find_all(text=" Big Data Developer "):
#     supername = str(tag.parent.name)
#     for tag1 in tag.parents:
#         parentum = tag1.name
#         supername = str(parentum) + '.' + supername
#     print(supername)

# print('\n\n\n')
# test_finding1 = soup.find(supername)
# print(test_finding1)


# list_of_obj1 = []
# for tag in soup.find_all(text=" Big Data Developer "):
#     list_of_obj1.append(tag)  


# list_of_obj2 = []
# for tag in soup.find_all(class_="font-weight-bold bigger"):
#     list_of_obj2.append(tag)
#     print(tag)

for article in soup.find_all("article"):
    job_name = article.find(class_="_15V35X").text
    job_company = article.find(class_="Ya0gV9").text
    print(job_name, job_company)


# list_of_obj3 =[]
# for tag in soup.find_all(class_="_15V35X"):
#     list_of_obj3.append(tag)
#     print(tag.text)

# for tag in soup.find_all(class_="Ya0gV9"):
#     print(tag.text)

# for tag in list_of_obj1:
#     for tag1 in tag.parents:
#         print(tag1.name)
#     print("\n")


# tag_title = soup.body.nfj-root.nfj-layout.nfj-main-content.div.nfj-posting-details.div.common-main-loader.main.article.div.common-posting-content-wrapper.div.common-posting-header.div.div.h1.h1

# soup.find(tag_title)
# print(tag_title)


# for element in parsedOffer.keys():
#     found_element = soup.find(element)
#     print(found_element)

# elem_1 = soup.find('posting-header')
# print(elem_1)


with open("page.html","w+", encoding="UTF-8") as f:
    f.write(soup.prettify())




#poczytaj o pakiecie scrapy



# Wstepny plan na utworzenie JSONa:
# 1. Znalezc potencjalne obiekty jako tagi bs4
# 2. Zapisac te potrzebne (pol)recznie do jakiegos pliku .txt
# 3. Nauczyc program pobierac szukane obiekty do pamieci z pliku .txt
# 4. Nauczyc program szukac tresci po wlasnie wczytanych do pamieci tagach
# 5. Zapisywac kolejne wyszukania w pliku tak, by calosc zapisywala sie w foramcie JSON

# Pytania:
# 1. Przede wszystkim, jakie są różnice między scrapy a BeautifulSoup?
# 2. Scrapy chyba lepiej jest w stanie zapisać plik do JSONa, z tego co czytałem. Tyle że, ten zapis działa chyba tylko gdy odpowiednio opdalać scrapy z konsoli. Więc, jak to zaimplemenotwać w kodzie??
# 3. Jak w odopowiedni sposób szukać/implementować odpowiednie ścieżki do wydobywania określonych treści, jak np. w moim przypadku Big Data Developer?
# 4. Uczyć się scrapy z tej stronki?

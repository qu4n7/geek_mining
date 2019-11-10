# Сергей, приветствую! Что то смог сделать с hh, avito не могу сделать.
# поскольку и так сильно задержал, сдаю, что получилось, иначе опять 
# упущу все остальное по курсу.
# если можно - после завершенного урока или курса - выкладывать ссылки на 
# правильные решение (или решения от студентов) - было бы супер. иначе, вряд
# ли я и такие как я, узнаю, как надо было решать заадчу.
# спасибо за проверку!


import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup
import lxml
import random
import pandas as pd

mongo_url = 'mongodb://localhost:27017'
client = MongoClient('localhost', 27017)
database = client.lesson2.hh
collection = database.hh

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36'

base_url = 'https://hh.ru/'
url = 'https://hh.ru/search/vacancy'
response = requests.get(url, headers={'User-Agent': USER_AGENT})

soup = BeautifulSoup(response.text, 'lxml')
body = soup.html.body

position = body.findAll(
    'div', attrs={'data-qa': 'vacancy-serp__vacancy vacancy-serp__vacancy_premium'}
)

names, wages, urls, site = [], [], [], []
missed = 0
for i in range(len(position)):
    names.append(
        body.findAll(
            'a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}
        )[i].text
    )
    if position[i].findAll('div', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'}) == []:
        wages.append('не указано')
        missed += 1
    else:
        wages.append(body.findAll(
            'div', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'}
        )[i-missed].text)
    urls.append(position[i].find("a").attrs["href"])
    site.append(url)
    
result = {
    'names': names,
    'wages': wages,
    'urls': urls,
    'site': site
}

print(pd.DataFrame(result))

collection.insert_one(result)

collection.insert_one(result)
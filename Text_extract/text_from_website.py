import pymongo
from pymongo import MongoClient
from selenium import webdriver
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer,TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
driver = webdriver.Chrome(r'C:\Users\jatoth.kumar\Downloads\chromedriver_win32 (1)\chromedriver.exe')
driver1 = webdriver.Chrome(r'C:\Users\jatoth.kumar\Downloads\chromedriver_win32 (1)\chromedriver.exe')
driver.get('https://www.ajio.com/s/fresh-men-aeropostale')
# driver.get('https://www.myntra.com/myntra-fashion-store?f=discount%3A50.0%3A%3Agender%3Amen%2Cmen%20women')
list_product = driver.find_elements_by_xpath('//a[@class="rilrtl-products-list__link"]')
# list_product = driver.find_elements_by_xpath('//div[@class="product-thumbShim"]')
description_1 = list_product[0].text
# print(len(list_product),description_1)
# [print(i.text) for i in list_product]
list2 = []
list4 = []
c = MongoClient('localhost',27017)
db = pymongo.MongoClient().webdata
for i in range(len(list_product)):
    print(list_product[i].get_attribute('href'))
    x = list_product[i].get_attribute('href')
    driver1.get(x)
    list3 = []
    list1 = driver1.find_elements_by_xpath('//ul[@class="prod-list"]/li')
    for j in range(len(list1)):
        print(list1[j].text)
        list3.append(list1[j].text)
        list4.append((list1[j].text))
    list2.append(list3)
    db.data1.insert({'data':list2[i]})
    print(list2[i])
    print('####') 

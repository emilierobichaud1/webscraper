from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import csv
import pandas as pd

driver = webdriver.Chrome("C:/Users/emili/chromedriver.exe")
driver.get("https://animalcrossing.fandom.com/wiki/Villager_list_(New_Horizons)")
time.sleep(30)

names = []
pics = []
types = []
species = []
birthdays = []
phrases = []
for i in range(1, 392):
    time.sleep(1)
    villager_name = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/table[2]/tbody/tr[2]/td/table/tbody/tr[{0}]/td[1]/b/a'.format(i)).get_attribute(
        "title")
    villager_pic = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/table[2]/tbody/tr[2]/td/table/tbody/tr[{0}]/td[2]/a/img'.format(i)).get_attribute(
        "src")
    villager_type = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/table[2]/tbody/tr[2]/td/table/tbody/tr[{0}]/td[3]/a'.format(i)).get_attribute(
        "title")
    villager_species = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/table[2]/tbody/tr[2]/td/table/tbody/tr[{0}]/td[4]/a'.format(i)).get_attribute(
        "title")
    villager_birthday = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/table[2]/tbody/tr[2]/td/table/tbody/tr[{0}]/td[5]'.format(i)).text
    villager_phrase = driver.find_element_by_xpath(
        '//*[@id="mw-content-text"]/table[2]/tbody/tr[2]/td/table/tbody/tr[{0}]/td[6]'.format(i)).text
    names.append(villager_name)
    pics.append(villager_pic)
    types.append(villager_type)
    species.append(villager_species)
    birthdays.append(villager_birthday)
    phrases.append(villager_phrase)

df = pd.DataFrame({'Name': names, 'Picture': pics, 'Personality': types, 'Species': species,
                   'Birthday': birthdays, 'Catchphrase': phrases})
df.to_csv('acnh.csv', index=False, encoding='utf-8')

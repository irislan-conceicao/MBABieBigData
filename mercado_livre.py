from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json


def finds(browser, by, expression):
    try:
        return browser.find_elements(by, expression)
    except NoSuchElementException as nse:
        return None

def find(browser, by, expression):
    try:
        return browser.find_element(by, expression)
    except NoSuchElementException as nse:
        return None
a=input("Selecione o item\n")
output  = open('output.json', 'w', encoding='utf-8')
driver = webdriver.Firefox()
driver.get("https://lista.mercadolivre.com.br/" + a)

items = finds(driver, By.CLASS_NAME, 'ui-search-result__content-wrapper')

for item in items: 
    descricao = find(item, By.CLASS_NAME, 'ui-search-item__title').get_property("textContent")
    preco = find(item, By.CLASS_NAME, 'ui-search-price').get_property("textContent")
    
    print(descricao)
    print(preco) 
    item = {'descricao': descricao, 'preco': preco}
    output.write(json.dumps(item))
    output.write('\n')

#-------------------------------------------------------------------------------
# Name:        ValidarPrecos
# Purpose:
#           Testedo selenium no python acessa o site do submarino procura pelo "produto"
#           e pega o preço e nome do primeiro item da lista
#
# Author:      Felipe Desiglo
#
# Created:     30/04/2017
# Copyright:   (c) Desiglo 2017
#-------------------------------------------------------------------------------
from selenium import webdriver
import time

Produto = "celular"

desired_caps = {}
desired_caps['platform'] = 'WINDOWS'
desired_caps['browserName'] = 'firefox'

browser = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=desired_caps)

browser.implicitly_wait(10)

#Submarino
browser.get('https://www.submarino.com.br/')
browser.find_element_by_id('h_search-input').send_keys(Produto)
browser.find_element_by_class_name('src-btn').click()
time.sleep(5)
item = browser.find_element_by_class_name('card-product-details')
itemText = item.find_element_by_class_name('card-product-name')
itemPrice = item.find_element_by_class_name('card-product-price').find_elements_by_class_name('value')[1]
print "Submarino:"
print itemText.text
print itemPrice.get_attribute('content')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from bs4 import BeautifulSoup
import re
import json

main_url = 'http://books.toscrape.com/'
count = 1
books_items = []

#Proceso que obtiene y retorna todas las categorías en formato json.
#Puede ser comprobado en la URL: http://localhost:8000/scraper/categories/
def category():
	url = main_url
	soup = get_soup(url)
	categories_container = soup.find(class_='side_categories')
	categories_list = categories_container.find('ul').find('ul').find_all('a')
	count = 1
	categories_items = []
	for category_item in categories_list:
	  item = {
	  		"id": count,
	  		"name": trim_text(category_item.get_text()),
	  		"url": url + category_item.get('href')
	  }
	  count += 1
	  categories_items.append(item)
	data = json.dumps(categories_items)
	return data

#Proceso que obtiene y retorna todos los libros, con sus respectivas categorías en formato json.
#Puede ser comprobado en la URL: http://localhost:8000/scraper/books/
def books():
	global books_items
	categories = json.loads(category())
	count = 1
	for category_content in categories:
		page = "index.html"
		url = category_content['url']
		category_id = category_content['id']
		soup = get_soup(url)
		
		while True:
			get_books(url,category_id)
			if(has_next(soup)):
				url = next_page_url(page,url,soup)
				page = next_page(soup)
				soup = get_soup(url)
			else:
				break
	data = json.dumps(books_items)
	return data

#funciones y procesos adicionales.
def trim_text(text):
	return re.sub(r'[\ \n]{2,}', '', text)

def get_soup(url):
	request = requests.get(url)
	soup = BeautifulSoup(request.text, 'html.parser')
	return soup

def has_next(soup):
	if (soup.find(class_="next")):
		return True
	return False

def next_page_url(page, url, soup):
	new_page = soup.find(class_="next").find('a')["href"]
	return url.replace(page,new_page)

def next_page(soup):
	page = soup.find(class_="next").find('a')["href"]
	return page

def get_books(url,category_id):
	global count
	global books_items
	soup = get_soup(url)
	books_container = soup.find('ol')
	books_list = books_container.find_all(class_="product_pod")

	for book in books_list:
		book_url = main_url + 'catalogue/' + book.find('h3').find('a')['href'].replace('../','')
		#Consulta la URL del libro individual, para extraer la descripción y otros datos.
		soup = get_soup(book_url)

		if (soup.find("div", {"id": "product_description"}) != None ):
			book_description = trim_text(soup.find("div", {"id": "product_description"}).find_next_sibling().get_text())
		else:
			book_description = ""

		if ("in stock" in trim_text(soup.find(class_="instock availability").get_text()).lower()):
			book_stock = True
		else:
			book_stock = False

		book_upc = trim_text(soup.find(text="UPC").parent.find_next_sibling().get_text())

		book_content = {
			"id": count,
			"category_id": category_id, #aquí va el id de categoría que viene por parámetro.
			"title": trim_text(soup.find(class_="product_main").find('h1').get_text()),
			"thumbnail_url":  main_url + book.find('img')['src'].replace('../',''),
			"price": trim_text(soup.find(class_='price_color').get_text()),
			"stock": book_stock,
			"product_description": book_description,
			"upc": book_upc
		}
		count += 1
		books_items.append(book_content)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from apps.scraper import scraping, models
from apps.scraper.models import Category, Book
import requests
from bs4 import BeautifulSoup
import re
import json

def save_books():
	categories = json.loads(scraping.category())

	books = json.loads(scraping.books())

	for item in categories:
		new_category = Category()
		new_category.id = item['id']
		new_category.name = item['name']
		new_category.url = item['url']
		new_category.save()
		del new_category

	for item in books:
		new_book = Book()
		new_book.id = item['id']
		new_book.category_id = Category.objects.get(id=item['category_id'])
		new_book.title = item['title']
		new_book.thumbnail_url = item['thumbnail_url']
		new_book.price = item['price']
		new_book.stock = item['stock']
		new_book.product_description = item['product_description']
		new_book.upc = item['upc']
		new_book.save()
		del new_book

	return "Las categorías y los libros han sido almacenados exitosamente."
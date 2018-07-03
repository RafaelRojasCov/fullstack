# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from apps.scraper import scraping
from apps.scraper import save_data


# Create your views here.

def scraper(request):
	return HttpResponse('Desde el Scraper')

def getCategories(request):
	return HttpResponse(scraping.category())

def getBooks(request):
	return HttpResponse(scraping.books())

def save(request):
	return HttpResponse(save_data.save_books())


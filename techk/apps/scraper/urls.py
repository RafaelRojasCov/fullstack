from __future__ import unicode_literals
from django.conf.urls import url, include
from apps.scraper import views

urlpatterns = [
    url(r'^$',views.scraper, name="scraper"),
    url(r'^categories/', views.getCategories, name="categories"),
    url(r'^books/', views.getBooks, name="books"),
    url(r'^save_books/', views.save, name="save books"),
]
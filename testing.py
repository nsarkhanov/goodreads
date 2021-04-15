import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import scraper

page_html = rq.get(
    "https://www.goodreads.com//book/show/1582996.City_of_Ashes")
i = BeautifulSoup(page_html.content, 'html.parser')
print(i)
i = "https://www.goodreads.com//book/show/618177.Legend"


def getlink(i):

    data_frame = []
    page_html = rq.get(i)
    page_soup = BeautifulSoup(page_html.content, 'html.parser')
    title = get_title(page_soup)

    author = get_author(page_soup)

    num_rating = get_num_rating(page_soup)

    num_reviews = get_num_reviews(page_soup)

    avg_rating = get_avg_rating(page_soup)

    num_pages = get_num_pages(page_soup)

    original_publish_year = get_original_publish_year(page_soup)

    series = get_series(page_soup)

    genres = get_genres(page_soup)

    award = get_award(page_soup)

    place = get_place(page_soup)
    dictionary = {
        "title": title,
        "author": author,
        "num_rating": num_rating,
        "num_reviews": num_reviews,
        "avg_rating": avg_rating,
        "num_pages": num_pages,
        "original_publish_year": original_publish_year,
        "series": series,
        "genres": genres,
        "award": int(award),
        "place": place,
        "url": i
    }
    data_frame.append(dictionary)
    return data_frame


getlink(i)

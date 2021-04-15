import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests as rq


def get_title(page_soup):
    try:
        title = page_soup.find('h1', {"id": "bookTitle"}).text.strip()
        return title
    except:
        return np.nan


def get_author(page_soup):
    try:
        author = page_soup.find("a", {"class": "authorName"}).text.strip()
        return author
    except:
        return np.nan


def get_num_rating(page_soup):
    try:
        num_rating = page_soup.find(itemprop="ratingCount").text.strip().replace(
            "ratings", "").replace(",", "")
        return int(num_rating)
    except:
        return np.nan


def get_num_reviews(page_soup):
    try:
        num_review = page_soup.find(itemprop="reviewCount").text.replace(
            "reviews", "").replace(",", "").strip()
        return int(num_review)
    except:
        return np.nan


def get_avg_rating(page_soup):
    try:
        avg_rating = page_soup.find(
            "span", itemprop="ratingValue").text.strip()
        return float(avg_rating)
    except:
        return np.nan


def get_num_pages(page_soup):
    try:
        num_pages = page_soup.find(
            itemprop="numberOfPages").text.strip().replace("pages", "")
        return int(num_pages)
    except:
        return 0


def get_original_publish_year(page_soup):
    try:
        original_publish_year = page_soup.find_all(
            "div", class_="row")[1].text.split()
        for i in original_publish_year[:]:
            if i.isnumeric() == True:
                return i
    except:
        return np.nan


def get_series(page_soup):

    try:

        series = page_soup.find(id="bookSeries").text.strip()
        if len(series) != 0:
            return True
        else:
            return False
    except:
        return np.nan


def get_genres(page_soup):
    try:
        g_list = []
        genres = page_soup.find(
            'div', class_="rightContainer").find_all(class_="left")
        for row in genres:
            row = row.text.replace(">", "").strip().split()
            row = " ".join(row)
            g_list.append(row)
        return g_list
    except:
        return np.nan


def get_award(page_soup):
    try:
        count = 0
        awards = page_soup.find("div", {"itemprop": "awards"}).find_all('a')
        for award in awards:
            if award != None:
                count += 1
        return count
    except:
        return 0


def get_place(page_soup):
    try:
        place = page_soup.find("div", {'id': "bookDataBox"}).find(
            'span', class_="darkGreyText").text.replace("(", "").replace(")", "").strip()
        return str(place)
    except:
        return np.nan

        # # End of Functions


def get_data_frame(links):
    data_frame = []
    for url in links:
        page_html = rq.get(url)
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
            "num_pages": int(num_pages),
            "original_publish_year": original_publish_year,
            "series": series,
            "genres": genres,
            "award": int(award),
            "place": place,
            "url": url
        }
        data_frame.append(dictionary)
    return data_frame


def get_books_url_per_page(base_url, tag, tag_class):
    book_url_list = []
    base_page = rq.get(base_url)
    base_content = BeautifulSoup(base_page.content, 'html.parser')
    for a in base_content.find_all(tag, class_=tag_class):
        book_url_list.append('https://www.goodreads.com/' + a['href'])
    return book_url_list


def get_base_page_list(base_url, n):
    base_page_list = []
    for i in range(n):
        base_page_list.append(base_url + str(i + 1))

    return base_page_list


def get_links():
    book_url_list = []
    for link in get_base_page_list('https://www.goodreads.com/list/show/1043.Books_That_Should_Be_Made_Into_Movies?page=', 1):
        book_url_list.append(get_books_url_per_page(link, 'a', 'bookTitle'))
    book_url_list = [link for subs in book_url_list for link in subs]
    return book_url_list

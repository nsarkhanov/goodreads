from libraries import *


def scraper(book):
    url_test = "https://www.goodreads.com/book/show/1582996.City_of_Ashes"
    data_test = requests.get(url_test)
    print(data_test)
    soup_test = BeautifulSoup(data_test.content, 'html.parser')

    titles = soup_test.find("h1", {"id": "bookTitle"}).text.strip()
    author = soup_test.find("a", {"class": "authorName"}).text.strip()
    num_rating = int(soup_test.find(itemprop="ratingCount").text.strip().replace(
        "ratings", "").replace(",", ""))
    num_reviews = int(soup_test.find(itemprop="reviewCount").text.strip().replace(
        "reviews", "").replace(",", ""))
    avg_rating = float(soup_test.find(
        "span", itemprop="ratingValue").text.strip())
    num_pages = int(soup_test.find(
        itemprop="numberOfPages").text.strip().replace("pages", ""))
    original_publish_year = soup_test.find_all(
        "div", class_="row")[1].text.split()[3]
    series = soup_test.find(id="bookSeries").text.strip()
    # print(series)
    if len(series) == 0:
        print(False)
    else:
        print(True)
    genres = soup_test.find(
        'div', class_="rightContainer").find_all(class_="left")
    for row in genres:
        row = row.text.replace(">", "").strip().split()
        row = " ".join(row)
        print(row)
    awards = soup_test.find("div", {"itemprop": "awards"}).find_all('a')
    count = 0
    for award in awards:
        if award != None:
            count += 1
    places = soup_test_2.find_all("a", class_="infoBoxRowItem")
    for place in places:
        print(place)

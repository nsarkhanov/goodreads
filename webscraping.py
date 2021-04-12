from libraries import *

data = requests.get(
    "https://www.goodreads.com/list/show/1043.Books_That_Should_Be_Made_Into_Movies")
print(data)
soup = BeautifulSoup(data.content, 'html.parser')

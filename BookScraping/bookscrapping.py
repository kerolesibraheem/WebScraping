import requests
from bs4 import BeautifulSoup

for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    see = soup.find('ol', {'class': 'row'})
    articles = see.find_all('article', {'class': 'product_pod'})

    for article in articles:
        image = article.find('img')
        final_title = image.attrs['alt']
        star = article.find('p')
        star_rating = star['class'][1]
        price = article.find('p', {'class': 'price_color'}).text
        print('Book info --> ', 'Name :', final_title, ', Price :', price, ', Star rating :', star_rating)


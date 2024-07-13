import requests
from bs4 import BeautifulSoup

url = "https://www.jumia.com.eg/ios-phones/"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

c = soup.find('div', {'class': '-paxs row _no-g _4cl-3cm-shs'})
ans = c.find_all('article', {'class': 'prd _fb col c-prd'})

for pt in ans:
    name = pt.find('a')
    name1 = name.find('div', {'class': 'info'})
    final_name = name1.find('h3', {'class': 'name'}).text
    price = pt.find('a')
    price1 = price.find('div', {'class': 'info'})
    final_price = price1.find('div', {'class': 'prc'}).text
    info = [final_name, final_price]
    print(info)

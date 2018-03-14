import requests
import csv
from bs4 import BeautifulSoup

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])
pages = []

for i in range(1, 6):
    url = 'https://www.nga.gov/collection/artists.html?const_startLetter=z&pageNumber=' + str(i) + '&lastFacet=const_startLetter'
    print(url)
    pages.append(url)
print(pages)
for item in pages:
    page = requests.get(item, timeout=(10, 20))
    print(page.text)
    soup = BeautifulSoup(page.text, 'html.parser')
    # last_links = soup.find(class_='AlphaNav')
    # last_links.decompose()
    artist_name_list = soup.find('ul', 'returns').find_all('a')
    for artist_name in artist_name_list:
        name = artist_name.contents[0]
        link = artist_name.get('href')
        # f.writerow([name, link])
        print(name)
        print(link)
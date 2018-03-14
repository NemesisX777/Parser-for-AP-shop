from bs4 import *

with open('ap_site_map.xml', 'r', encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'xml')



print(len(soup.contents))

from bs4 import *

with open('test_web_page_01_unspaced.html', 'r', encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'lxml')

images = []
attributes = {}

item_name = str(soup.find('h1').string)
sku = str(soup.find('div', 'sku').contents[1])
short_descr = str(soup.find('div', 'short-description').find('div', 'std'))
# additional_info = str(soup.find('div', 'short-description').find('div', 'std').contents[0])
price = str(soup.find('meta', itemprop="price")['content'])
availability = str(soup.find('p', "availability in-stock").contents[1].contents[1])
for link in soup.findAll('a', 'cloud-zoom-gallery lightbox-group'):
    images.append(link.get('href'))
for attrib in soup.find('table', id='product-attribute-specs-table').find('tbody').find_all('tr'):
    attrib_name = str(attrib.th.contents[0])
    attrib_value = str(attrib.td.contents[0])
    attributes[attrib_name] = attrib_value

print(item_name)
print(sku)
print(short_descr)
# print(additional_info)
print(price)
print(availability)
print(images)
print(attributes)

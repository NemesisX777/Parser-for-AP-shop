from bs4 import BeautifulSoup
import csv

with open('ap_for_clients.xml', 'r', encoding='utf8') as fp:
    soup = BeautifulSoup(fp, 'xml')

with open('offer_from_xml.csv', 'w', newline='', encoding='utf8') as csvfile:
    f = csv.writer(csvfile, dialect='excel')
    f.writerow(['name', 'vendor', 'price', 'category_id', 'url', 'picture', 'availability'])

    for products in soup.find_all('offer'):
        name = str(products.model.string)
        vendor = str(products.vendor.string)
        price = str(products.price.string)
        cat = str(products.categoryId.string)
        url = str(products.url.string)
        pic = str(products.picture.string)
        avail = str(products['available'])

        f.writerow([name, vendor, price, cat, url, pic, avail])

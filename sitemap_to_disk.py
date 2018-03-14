import requests

url = 'https://aquapolis.ru/sitemap.xml'
page = requests.get(url)

f = open('ap_site_map.xml', 'w', encoding='utf8')
f.write(page.text)
f.close()

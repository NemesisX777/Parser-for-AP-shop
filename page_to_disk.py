import requests

url = 'https://aquapolis.ru/nasos-aquaviva-bqp-4-0-trehfaznyj.html'
page = requests.get(url)

f = open('test_web_page_01.html', 'w', encoding='utf8')
f.write(page.text)
f.close()

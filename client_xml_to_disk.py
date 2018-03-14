import requests

url = 'https://aquapolis.ru/export/get/file/id/forpartners'
page = requests.get(url)
page.encoding = "cp1251"  # указываем кодировку скачанного файла
page_txt = page.text
page_txt = page_txt.replace("windows-1251", "utf-8")  # мен¤ем содержимое

with open('ap_for_clients.xml', 'w', encoding='utf-8') as f:
    f.write(page_txt)

# print(page.status_code)
# print(page.headers)
# print(page.encoding)

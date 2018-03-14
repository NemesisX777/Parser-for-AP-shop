from bs4 import *

f = open('test_web_page_01.html', 'r', encoding='utf8')
page = f.read()
f.close()

soup1 = str(BeautifulSoup(page, 'html.parser'))
soup2 = str(BeautifulSoup(page, 'lxml'))
soup3 = str(BeautifulSoup(page, 'xml'))
soup4 = str(BeautifulSoup(page, 'html5lib'))

f = open('test_web_page_htmlparser.html', 'w', encoding='utf8')
f.write(soup1)
f.close()

f = open('test_web_page_lxml.html', 'w', encoding='utf8')
f.write(soup2)
f.close()

f = open('test_web_page_xml.html', 'w', encoding='utf8')
f.write(soup3)
f.close()

f = open('test_web_page_html5.html', 'w', encoding='utf8')
f.write(soup4)
f.close()
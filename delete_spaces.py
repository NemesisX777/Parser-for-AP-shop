import re

with open('test_web_page_01.html', 'r', encoding='utf8') as fs:
    page = fs.read()

regex = re.compile('$\s+', re.MULTILINE)
ready_html = re.sub(regex, '', page)

with open('test_web_page_01_unspaced.html', 'w', encoding='utf8') as ff:
    ff.write(ready_html)

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.title, "\n")
print(soup.title.name, "\n")
print(soup.title.string, "\n")
print(soup.title.parent.name, "\n")
print(soup.p, "\n")
print(soup.p['class'], "\n")
print(soup.a, "\n")
print(soup.find_all('a'), "\n")
print(soup.find(id="link3"), "\n")

for link in soup.find_all('a'):
    print(link.get('href'))
print("\n")

head_tag = soup.head
print(head_tag)
print(head_tag.contents)
print(head_tag.string)

print("\n")

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)
print(title_tag.string)


# print("\n")
#
# for child in title_tag.children:
#     print(child)
#
# print("\n")
#
# for child in head_tag.descendants:
#     print(child)

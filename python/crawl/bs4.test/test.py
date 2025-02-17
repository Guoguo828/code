from bs4 import BeautifulSoup

with open("./test.html", encoding="utf-8") as fin:
    html_doc = fin.read()

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)
divenode = soup.find('div')
print(divenode)
links = divenode.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())
    
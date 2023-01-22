from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://ong-zijian.github.io/zijian_personal_page/"
page = urlopen(url)
html = page.read().decode("utf-8")
#create beautifulsoup object and assign to soup
soup = BeautifulSoup(html, "html.parser")
print(soup)
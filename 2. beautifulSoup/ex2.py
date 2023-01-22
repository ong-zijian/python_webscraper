from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

routerTags = soup.find_all("a")

router = []

for line in routerTags:
    router.append(line['href'])

for i in range(0, len(router)):
    router[i] = "http://olympus.realpython.org" + router[i]
    
print(router)

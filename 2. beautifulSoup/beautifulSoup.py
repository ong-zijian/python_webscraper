from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
#create beautifulsoup object and assign to soup
soup = BeautifulSoup(html, "html.parser")

#print(soup.get_text())

#print(soup.find_all("img"))

image1, image2 = soup.find_all("img")

# .name property. Returns 'img' in this case
print(image1.name)

#HTML properties, using src, or even alt
#returns '/static/dionysus.jpg'
print(image1["src"])

#returns '/static/grapes.png'
print(image2["src"])

#call by html tags
#returns '<title>Profile: Dionysus</title>'
print(soup.title)

#retrieve the string inside the tag
#returns 'Profile: Dionysus'
print(soup.title.string)

#Search for a specific kind of tag that has a value
#returns [<img src="/static/dionysus.jpg"/>]
print(soup.find_all("img", src="/static/dionysus.jpg"))


import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"

#page is a response object that stores the response from requesting the URL from the browser
page = browser.get(url)

#MechanicalSoup uses BeautifulSoup to parse the HTML from the request, and page has a .soup attribute that represents a BeautifulSoup object
# # print(type(page.soup))
# # print(page.soup)

#username: zeus
#password: ThunderDude
#Fill up and submit form using Python
# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

#returns 'http://olympus.realpython.org/profiles' as the page has been logged in
#print(profiles_page.url)

########################################################################################################################
#obtaining the url
links = profiles_page.soup.select('a')

#returns:
'''
Aphrodite: http://olympus.realpython.org/profiles/aphrodite
Poseidon: http://olympus.realpython.org/profiles/poseidon
Dionysus: http://olympus.realpython.org/profiles/dionysus
'''
for link in links:
    address = link['href']
    text = link.text
    print(f"{text}: {address}")


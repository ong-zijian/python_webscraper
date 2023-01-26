"""
This Selenium Scraper is retrieved directly from: https://www.browserstack.com/guide/web-scraping-using-selenium-python
All credits to BrowserStack.com I do not own any part of the code

Note to self:
This Selenium webscraper is a search style web scrapper which finds keywords and their occurences. 
Other tools will be needed to perform component scrapping and or form handling
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

# Obtain the version of ChromeDriver compatible with the browser being used.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Obtain the url and scrape
val = input("Enter a url: ")

# wait for the page to load
wait = WebDriverWait(driver, 10)


driver.get(val)

get_url = driver.current_url
wait.until(EC.url_to_be(val))


if get_url == val:
    page_source = driver.page_source

# using beatifulsoup to parse the HTML content obtained
soup = BeautifulSoup(page_source, features="html.parser")
keyword = input("Enter a keyword to find instances of in the article:")
matches = soup.body.find_all(string=re.compile(keyword))

len_match = len(matches)

title = soup.title.text

# Store the data collected into a text file
# codec to open text file titled article_scraping
file = codecs.open('article_scraping1.txt', 'a+')
file.write(title+"\n")
file.write("The following are all instances of your keyword:\n")

count = 1

for i in matches:
    file.write(str(count) + "." + i + "\n")
    count += 1

file.write("There were "+str(len_match)+" matches found for the keyword.")
file.close()
driver.quit()


"""
https://www.scrapingbee.com/blog/selenium-python/
https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
"""

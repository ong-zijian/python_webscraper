#write a simple program that opens the dice page and scrapes the result
import mechanicalsoup


#select method to find id=result hence the '#result'
browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")
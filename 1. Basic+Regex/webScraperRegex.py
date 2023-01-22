import re
from urllib.request import urlopen
#.findall() finds text within a string
'''
First Argument(1):
- regular expression you want to match
Second Argument(2):
- String to test

regex "ab*c" matches any part of "ac" that begins with 'a' and ends with 'c'

'''
re.findall("ab*c", "ac") #returns ["ac"]

re.findall("ab*c", "abcd") #returns ["abc"]

re.findall("ab*c", "acc") #returns ["ac"]

re.findall("ab*c", "abcac") #returns ["abc", "ac"]

re.findall("ab*c", "abdc") #returns []


##################################################################################################
#.IGNORECASE ignores cases

re.findall("ab*c", "ABC", re.IGNORECASE) #returns ['ABC]


##################################################################################################
# .* in regex stands for any character repeated any number of times.

re.findall("a.*c", "abc") #returns ['abc']
 
re.findall("a.*c", "abbc") #returns ['abbc']

re.findall("a.*c", "ac") #returns ['ac']

re.findall("a.*c", "acc") #returns ['acc']


##################################################################################################
# re.search to find a particular pattern in a string
# returns an object called matchObject that stores different groups of data
#use .group() on match object will return the first and most inclusive result, which in most cases is just what you want

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
match_results.group() # returns "ABC'


###################################################################################################
# re.sub() is like a replace() method

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>", "ELEPHANTS", string)
# returns 'Everything is ELEPHANT'
# <.*> is a greedy implementation and would replace from the first '<' to '>'

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "ELEPHANTS", string)
#returns "Everything is ELEPHANTS if it's in ELEPHANTS."
# <.?> is a less greedy implementation and replaces each and every one of it


####################################################################################################
#Extract Text From HTML With Regular Expressions
#HTML Source file: <TITLE >Profile: Dionysus</title  / >
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
from urllib.request import urlopen

url = "https://ong-zijian.github.io/zijian_personal_page/"
#Open the url declared above and shows a response like below
'''>>> page
<http.client.HTTPResponse object at 0x105fef820>'''
page = urlopen(url)

#read method which returns a sequence of bytes and .decode() will decode them to strings using UTF-8
html_bytes = page.read()
html =html_bytes.decode("utf-8")

print(html)

#finding the index of the tag and then the index of the first character in the tag
title_index = html.find("<title>")
start_index = title_index + len("<title>")

#finding the end index. Since the numbering starts from 0 and the way python slices string, you need the index of the last character + 1 which is the end_index itself
end_index = html.find("</title>")

#slice and print
title = html[start_index:end_index]
print(title)



#Source and Credits: https://realpython.com/python-web-scraping-practical-introduction/
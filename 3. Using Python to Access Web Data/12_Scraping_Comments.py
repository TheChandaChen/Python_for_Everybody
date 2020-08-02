import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0

# Retrieve all span tags
spans = soup('span')

# Split span tags to only have numbers
for span in spans:
    string = str(span)
    comments_split = string.split('>')
    comments_unfinished = comments_split[1]
    comments_split_twice = comments_unfinished.split('<')
    comments = comments_split_twice[0]
    comments = int(comments)
    sum = sum + comments

print(sum)

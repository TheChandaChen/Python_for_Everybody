import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# All inputs from the user + changing type to integer
url = input('Enter URL: ')
count = input('Enter count: ')
count = int(count)
position = input("Enter position: ")
position = int(position) - 1

# Loop that follows the links
while count > 0:
    count -= 1   # Count of how many times we followed the links

    # Requests the html from link
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieves all anchor tags
    tags = soup('a')

    # Finds the link position we are after
    print(tags[position].get('href', None))
    # Replaces url with it to continue the loop
    url = tags[position].get('href', None)

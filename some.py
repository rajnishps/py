import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link = input('enter url')
pos = int(input('enter Position'))
counts = int(input('enter the Count'))

while pos != 0:
    url = (link)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    count=counts
    tags = soup('a')
    for tag in tags:
        if count == 0:
            continue
        count -= 1
        link = (tag.get('href', None))
    
    pos -= 1

    print(link)

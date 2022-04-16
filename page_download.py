
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__=="__main__":

    #
    hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
    URL = 'https://h-pdm001.atlassian.net/wiki/spaces/A21/pages/60883657/Survey+VPN'

    # Using requests
    html = requests.get(url=URL, headers=hdr).text
    with open('output/page.txt', 'w') as file:
        file.write(html)

    # Using urllib
    page = urlopen(URL)
    doc = page.read().decode('utf-8')
    with open('output/page.txt', 'w') as file:
        file.write(doc)

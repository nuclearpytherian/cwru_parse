import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os


class Downloader:

    def __init__(self, EXPORT_PATH):
        self.EXPORT_PATH = EXPORT_PATH
        self.makedir(EXPORT_PATH)

    def __call__(self, URL):
        sourcecode = urllib.request.urlopen(URL).read()
        soup = BeautifulSoup(sourcecode, "html.parser")
        td_list = soup.find_all('td')

        for td in td_list:
            if td.find('a') is not None:
                href = td.find('a')['href']
                if href is not None:
                    text = td.text
                    try:
                        urllib.request.urlretrieve(href, f"{self.EXPORT_PATH}/{text}.mat")
                        print(f"{text} is done. \n")
                    except Exception as e:
                        print(e)
                        print(f"{text} aborted. \n")

    def makedir(self, path):
        if not os.path.isdir(path):
            os.makedirs(path, exist_ok=False)


if __name__=="__main__":

    # Parameters
    URL = "https://engineering.case.edu/bearingdatacenter/48k-drive-end-bearing-fault-data"
    EXPORT_PATH = 'output/48k-drive-end-bearing-fault-data'

    # RUN
    download = Downloader(EXPORT_PATH=EXPORT_PATH)
    download(URL)



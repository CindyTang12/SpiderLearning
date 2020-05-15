import requests
from bs4 import BeautifulSoup
import re

url = 'https://python123.io/ws/demo.html'


def getText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Fail')


def find_all_tag_name(soup):
    for tag in soup.find_all(True):
        print(tag.name)


def find_tag_name_start_with_b(soup):
    for tag in soup.find_all(re.compile('b')):
        print(tag.name)


if __name__ == "__main__":
    demo = getText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    # find_all_tag_name(soup)
    # print("------------------------")
    # find_tag_name_start_with_b(soup)
    print(soup.find_all(string='Python'))

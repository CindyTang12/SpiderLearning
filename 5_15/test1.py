import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'


def getText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Fail')


if __name__ == "__main__":
    demo = getText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

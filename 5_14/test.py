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


def getChildren(soup):
    count = 1
    for child in soup.body.children:
        print(count, ":", child)
        count = count + 1


def getParents(soup):
    count = 1
    for parent in soup.a.parents:
        if parent is None:
            print(count, ":", parent)
        else:
            print(count, ":", parent.name)
        count = count + 1


def getSibling(soup):
    count = 1
    for sibling in soup.a.next_siblings:
        print(count, ":", sibling)
        count = count + 1


if __name__ == "__main__":
    demo = getText(url)
    soup = BeautifulSoup(demo, 'html.parser')
    getChildren(soup)
    print("================================")
    getParents(soup)
    print("================================")
    getSibling(soup)

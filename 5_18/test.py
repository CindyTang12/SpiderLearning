import requests
from bs4 import BeautifulSoup
import bs4
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


if __name__ == '__main__':
    url = 'http://so.cfi.cn/so.aspx?txquery=sh501305'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', attrs={'class': 'quote'})
    tds = table.find_all('td')
    info = {}
    stock_name = (tds[0].text.split()[0])
    info.update({'股票名称': stock_name})
    for td in tds:
        try:
            info.update({td.text.split(':')[0]:td.text.split(':')[1]})
        except:
            continue
    with open('/Users/Cindy/Desktop/stock.csv', 'a', encoding='utf-8') as f:
        f.write(str(info) + '\n')

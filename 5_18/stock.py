import requests
from bs4 import BeautifulSoup
import bs4
import re
import traceback


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockNum(ls, url):
    html = getHTMLText(url)
    soup = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r's[hz]\d{6}')
    for i in soup.find_all('a'):
        try:
            href = i.attrs['href']
            info = pattern.findall(href)[0]
            ls.append(info)
        except:
            continue


def getStockInfo(ls, url, path):
    for stock_name in ls:
        stock_url = url + stock_name
        html = getHTMLText(stock_url)
        soup = BeautifulSoup(html, 'html.parser')
        try:
            table = soup.find('table', attrs={'class': 'quote'})
            if table is None:
                continue
            tds = table.find_all('td')
            info = {}
            stock_name = (tds[0].text.split()[0])
            info.update({'股票名称': stock_name})
            for td in tds:
                try:
                    info.update({td.text.split(':')[0]: td.text.split(':')[1]})
                except:
                    continue
            with open(path, 'a', encoding='utf-8') as f:
                f.write(str(info) + '\n')
        except:
            traceback.print_exc()
            continue



def main():
    stock_num_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'http://so.cfi.cn/so.aspx?txquery='
    output_path = '/Users/Cindy/PycharmProjects/SpiderLearning/5_18/stock.csv'
    infols = []
    getStockNum(infols, stock_num_url)
    getStockInfo(infols, stock_info_url, output_path)

main()

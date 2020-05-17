import requests
import re


def getHTMLText(url):
    try:
        header = {
            'authority': 's.taobao.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cookie': 'hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; lgc=%5Cu661F%5Cu8349%5Cu4E0D%5Cu662F%5Cu8349; tracknick=%5Cu661F%5Cu8349%5Cu4E0D%5Cu662F%5Cu8349; tg=0; enc=5WO4yTuzoCYU4ZovRkRXEy1hNlCroaeWWJlIbUEP3BhMOqUqg51xcVZFKEC7TZ45YWrUrkBKr%2BRafjRNHSVVtQ%3D%3D; miid=1715154992670629735; cna=9Cr3FgSodyQCASQEnpItVQ/x; UM_distinctid=171d012bfb617a-0b4552dc0c38a2-30657701-13c680-171d012bfb71a5; t=589cb708fa5caee2b95519914bebfc98; sgcookie=EBpfr4FhiWiBNDFgtWv2e; uc3=nk2=s0%2BBNcUsWy99NQ%3D%3D&id2=UUGk2VB%2FwR47Ow%3D%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D&vt3=F8dBxGXEmrH8hk5dYnU%3D; uc4=nk4=0%40sTB3VtbIszgfTd0NHWSpMuFR%2B0Rk&id4=0%40U2OT6ZfdC4a9a81hmrmrP8Ga9Py%2B; _cc_=U%2BGCWk%2F7og%3D%3D; tfstk=cJxPBsmmkMAjfcivWgIFde70R3_RZ8KMvSWCrF9joYGtkOQlilNdnr7GuN1tmaf..; mt=ci=61_1; v=0; cookie2=1a7e3552b0dd66155c60f8e286fb9eab; _tb_token_=fd75f05e3ab9e; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _nk_=%5Cu661F%5Cu8349%5Cu4E0D%5Cu662F%5Cu8349; uc1=cookie14=UoTUM2cVHyqWaA%3D%3D; JSESSIONID=2C7CEAF5245BE99A48D257D82DFCF792; l=eB_1rFWqqefD4weCBOfaPurza779bIRYnuPzaNbMiT5PO35p5qbNWZAXdr89CnhNh6JeR3ucM4eWBeYBcIv4n5U62j-laTMmn; isg=BLe3WxcfpU9JfyLJWulx5fD4Rq0BfIveK-MsEAlkxgbtuNf6EU72LsuanxDmamNW',
        }
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ls, html):
    try:
        pattern_price = re.compile(r'\"view_price\"\:\"\d+\.\d*\"')  # "view_price":"279.00"
        pattern_title = re.compile(r'\"raw_title\"\:\".*?\"')  # "raw_title":"Oece2020夏装新款女装 少女复古减"
        plt = pattern_price.findall(html)
        tlt = pattern_title.findall(html)
        for i in range(len(plt)):
            price = plt[i].split('\"')[3]
            name = tlt[i].split('\"')[3]
            ls.append([name, price])
    except:
        print("解析出错")


def printGoodList(ls, num):
    print("=====================================================================================================")
    tplt = "{0:<3}\t{1:<30}\t{2:>6}"
    print(tplt.format("序号", "商品名称", "价格"))
    count = 0
    for g in ls:
        count += 1
        if count <= num:
            print(tplt.format(count, g[0], g[1]))
    print("=====================================================================================================")


def main():
    goodname = input("输入你想在淘宝网搜索的商品名称 ： ")
    depth = 2
    num = int(input("输入您想获取的商品数量 ："))
    infols = []
    for i in range(depth):
        url = "https://s.taobao.com/search?q=" + goodname + "&s=" + str(i * 44)
        html = getHTMLText(url)
        parsePage(infols, html)
    printGoodList(infols, num)


main()

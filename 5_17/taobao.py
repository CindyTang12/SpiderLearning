import requests
import re


def getHTMLText(url):
    try:
        headers = {
            'cookie': 'miid=1296267545453648768; t=b4d385e2145f596a67961e4dd08e9a8f; cna=pqwcFXxbJjACAXWIA7AFEfA8; thw=cn; tracknick=tb487881011; lgc=tb487881011; _cc_=UIHiLt3xSw%3D%3D; tg=0; enc=%2FTqA3gAexHOKU0cyPYbSWM1pGS8vgnlEK3EMnkYd2T%2BlB%2BJh18hxryREG48c%2BYmdk7yfvbSMCBDQExP23eUm3w%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=19ef67fdfc3f433776e5e9cafaf6a8ea; v=0; _tb_token_=08b7e3e7e183; _m_h5_tk=62383241b06635c64b07942e50e47d9d_1562004576179; _m_h5_tk_enc=0465da475a8335f8fd8d9ef6bb280a71; unb=4235284520; sg=101; _l_g_=Ug%3D%3D; skt=c571ae590b7580cb; cookie1=AnQIvxj44XbyESoVNTVtwfJRB8W%2BbAPV%2BVZMWhAghjk%3D; csg=23f40375; uc3=vt3=F8dBy34cs3fc7ebsEqk%3D&id2=Vy67WD1MZomrsw%3D%3D&nk2=F5RBzeKtOazPVJc%3D&lg2=UtASsssmOIJ0bQ%3D%3D; existShop=MTU2MTk5NTE3MQ%3D%3D; dnk=tb487881011; _nk_=tb487881011; cookie17=Vy67WD1MZomrsw%3D%3D; mt=ci=21_1; uc1=cookie14=UoTaGdT0tHdY5w%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=VFC%2FuZ9aj3yE&tag=8&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; whl=-1%260%260%261561995222497; isg=BHNzJqpkKgCWtOesccf13ZRUAnddACwkF8iwAyUQzxLJJJPGrXiXutG23hRvn19i; l=bBMxcfBPv539-OTkBOCanurza77OSIRYYuPzaNbMi_5K-6T_2qQOkAuQFF96Vj5Rs4YB4G2npwJ9-etkq',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        r = requests.get(url, headers=headers)
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
        print(html)
        # parsePage(infols, html)
    printGoodList(infols, num)


main()

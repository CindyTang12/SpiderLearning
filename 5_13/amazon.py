import requests

url = "https://www.amazon.cn/dp/B07FLZNKG6/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=2CZ9O7DTU45LV&keywords=%E5%9B%B4%E5%9F%8E&qid=1589369406&sprefix=%E5%9B%B4%E5%9F%8E%2Caps%2C168&sr=8-1"
kv = {'user-agent': 'Mozilla/5.0'}
try:
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('Fail')

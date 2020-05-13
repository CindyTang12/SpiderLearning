import requests
kv = {'wd' : '周深'}
url = "http://www.baidu.com/s"
try:
    r = requests.get(url, params = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print('Fail')

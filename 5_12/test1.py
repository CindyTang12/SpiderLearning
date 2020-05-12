import requests


def getHTMLText(url):
    try:
        r = requests.request('HEAD', url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.headers
    except:
        return "ERROR"


if __name__ == "__main__":
    url = "https://baidu.com"
    print(getHTMLText(url))

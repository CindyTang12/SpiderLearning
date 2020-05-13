import requests
import os
url = "https://p1.pstatp.com/large/pgc-image/38182469d82346afb04a09a09e6a8899"
root = "/Users/Cindy/Desktop/"
path = root + url.split('/')[-1] + ".png"
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('Successfully saved image.')
    else:
        print('File already existed.')
except:
    print('Failed to get the picture.')

import re
from urllib import request

url = 'http://sc.chinaz.com/tupian/'

req = request.Request(url)

resp = request.urlopen(req)

html = resp.read().decode()

# print(html)

imgs = re.findall(r'<div>.*?<a target="_blank" href="(.*?)" alt="(.*?)"', html, flags=re.S)

print(imgs)

# for img in imgs:
#     print(img[0])
#     request.urlretrieve(img[0], filename='../zhanzhangimg/{}.jpg'.format(img[1]))


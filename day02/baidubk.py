# 读取百度百科的网页
# 将网页存放到当前 ./html/目录下
# import re
from _md5 import md5
from urllib import request

# url = 'https://baike.baidu.com/'
#
# response = request.urlopen(url)
#
# if response.status == 200:
#
#     s = response.read().decode()
#
#     # print(re.match(r'html', s))
#
#     request.urlretrieve(url, './spider_data/b.html')  # 这种方式直接将rul的内容直接写入到指定的文件中
#
#     with open('spider_data/a.html', 'w') as f:
#         f.write(s)


# 基于md5生成新的图片名
# request.urlretrieve(img_url, './imgs/img1.png')

import hashlib
img_url = 'http://www.doc88.com/snapshot/home/1024489140.png'
print(img_url)
img_part = img_url.split('/')[-1].split('.')
new_str = hashlib.md5(img_part[0].encode()).hexdigest()
old_str = img_part[0]
# print(new_str)
# print(old_str)
new_img_url = img_url.replace(old_str, new_str)
print(new_img_url)














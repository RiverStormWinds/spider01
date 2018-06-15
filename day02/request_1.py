
# 爬取百度首页
import re
from urllib import request

# 1. 确定百度首页地址(url)
url = 'http://www.baidu.com'

# 2. 开始请求url，获取网页内容及网页资源
response = request.urlopen(url)  # 返回响应数据，字节码数据

# 3. 判断请求是否成功
# print(response.getcode())  # response.status 也可以查看响应数据，一个通过属性，一个通过方法

# 4. 从响应中读取网页内容
# print(response.readline())  # 拿到网页中的一行数据

# print((b''.join(response.readlines())).decode())  # 拿到整个网页数据内容

# print(response.read().decode())  # 读取字节码数据

s = response.read().decode()
# p1 = r'[\d]+'
p1 = r'<[\w]+>'


pattern1 = re.compile(p1)           # 我们在编译这段正则表达式
matcher1 = re.findall(pattern1, s)  # 在源文本中搜索符合正则表达式的部分

print(matcher1)

# print(s)
# with open('./spider_data/When.html', 'w', encoding='utf-8') as f:
#     f.write(s)


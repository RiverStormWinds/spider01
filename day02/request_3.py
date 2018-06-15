from urllib import parse, request

url = 'http://www.baidu.com/s?wd='
print(parse.quote(url))  # quote(url) 是专门用于中文编码

query = parse.quote('太空旅行')  # url编码

# print(parse.unquote(query))  # url解码

response = request.urlopen(url+query)
print(response.read().decode())

if response.status == 200:
    request.urlretrieve(url+query, '../spider_data/space_travel.html')

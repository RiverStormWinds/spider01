from urllib import parse, request

url = 'http://www.baidu.com/s?'

# url编码：http://www.baidu.com/s?wd=%E5%A4%AA%E7%A9%BA%E8%A7%86%E9%A2%91

# print(parse.urlencode('太空视频', encoding='utf-8'))

query = parse.urlencode({'wd': '太空视频', 'user': '扣扣'})  # 将汉字解码成浏览器识别的url形式

print(url + query)
# url编码：wd=%E5%A4%AA%E7%A9%BA%E8%A7%86%E9%A2%91&user=%E6%89%A3%E6%89%A3
# urlopen(url, data=b'')，如果是post请求时，需要用到data
resp = request.urlopen(url+query)  # data是post请求，且必须是字节类型data=query.encode()

if resp.getcode() == 200:
    request.urlretrieve(url+query, './spider_data/space.html')

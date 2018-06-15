from urllib import parse, request

url = 'http://fanyi.baidu.com/sug'

data = {
    'kw': '何'
}

params = parse.urlencode(data)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 '
                  'Firefox/60.0Accept: text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,*/*;q=0.8z'

}

# 生成请求对象
# Request(url=, data=, headers=)
# data数据要求是bytes，存在data时，表示请求为post请求
req = request.Request(url, params.encode(encoding='utf-8'), headers)

# 发起请求
resp = request.urlopen(req)
if resp.status == 200:
    print('请求成功')
    print('--数据--', resp.read().decode())


    # with open('fruit.json', 'wb') as f:
    #     f.write(resp.read())

    print('保存fruit.json成功')

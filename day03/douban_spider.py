from urllib import parse, request

# url ='https://movie.douban.com/j/subject_suggest'

url = 'https://movie.douban.com/subject_search?'

data = {
    'search_text': '动漫',
    'cat': '1002'
}

params = parse.urlencode(data)

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 '
                      'Firefox/60.0Accept: text/html,application/xhtml+xml,'
                      'application/xml;q=0.9,*/*;q=0.8z',
    'Cookie': 'll="108288"; bid=ZUbY1CnkPek; __utma=30149280.1640882581.1528861793.1528861793.1528861793.1; __utmb=30149280.4.10.1528861793; __utmc=30149280; __utmz=30149280.1528861793.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=bejson; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1528861817%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_id.100001.4cf6=7abe7e5ad1f514f4.1528861817.1.1528861918.1528861817.; _pk_ses.100001.4cf6=*; __yadk_uid=Z192W7DHd7ROTqtEXZw8rppjWxteU76M; __utma=223695111.1049808133.1528861818.1528861818.1528861818.1; __utmb=223695111.0.10.1528861818; __utmc=223695111; __utmz=223695111.1528861818.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _vwo_uuid_v2=D691807051801ACF4572FF61D0ED75955|a0d2a0239905832ce27b11c7d4cfa279'
}

req = request.Request(url+params, headers=header)
resp = request.urlopen(req)
print(resp.read().decode())

# 人人网－登录、获取个人信息
# 登录url
import json
from http import cookiejar
from urllib import request, parse

login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018531751133'
# http://www.renren.com/PLogin.do
# login_url = 'http://dj.renren.com/seostat'

loginParams = {
    'key_id': '1',
    'f': 'http://www.renren.com/958915617/profile',
    'icode': '',  # 验证码内容
    'rkey': '22f7e231f87f85b2bd296fb2257b6e2d',
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'captcha': 'web_login',
    'email': '17791692095',
    'password': '9d3b314ddad11935ae8ea2849bd53afb1383155d0110a5d22c6a8de3570d67b0'
}

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:60.0) Gecko/20100101 Firefox/60.0'
}

# 实现用户登录
# 1. 创建CookieJar对象
cookieJar = cookiejar.CookieJar()

# 2. 创建可处理Cookie的Handler
handler = request.HTTPCookieProcessor(cookieJar)

# 3. 创建请求的opener对象
opener = request.build_opener(handler)

# 4. 创建请求对象
params = parse.urlencode(loginParams)
loginReq = request.Request(url=login_url,
                           data=params.encode(), headers=headers)

# 5. 发起登录的请求
resp = opener.open(loginReq)

bytes = resp.read()
print(bytes.decode('utf-8'))
jsonObj = json.loads(bytes.decode('utf-8'))
print(jsonObj.get('failDescription'))

import json
from http import cookiejar
from urllib import request, parse

#  [Full request URI: http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018532325953]

login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018532325953'

login_params = {
    "email": "13720430615",
    "icode": "导争似红",
    "origURL": "http://www.renren.com/home",
    "domain": "renren.com",
    "key_id": "1",
    "captcha_type": "web_login",
    "password": "91f2b76a56f0a16ab4b7ff0375540ea9b9cde75c8c2fd664de9acb5456b82f3b",
    "rkey": "a71814af6f7a4a5ebef6d6ee2f13dda9",
    "f": ""
}

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv: 60.0) Gecko / 20100101Firefox / 60.0',
}

cookieJar = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookieJar)
opener = request.build_opener(handler)
params = parse.urlencode(login_params)
loginReq = request.Request(login_url, params.encode(), headers)

resp = opener.open(loginReq)

bytes = resp.read()

print(bytes.decode('utf-8'))

jsonObj = json.loads(bytes.decode('utf-8'))

print(jsonObj)

# print(jsonObj.get('failDescription'))
























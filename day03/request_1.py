

# 设置请求头信息
from urllib.request import Request, urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context  # 上下文直接默认为安全上下文，让默认上下文转变为未认证上下文
# 解决 error [SSL: CERTIFICATE_VERIFY_FAILED] 证书认证失败

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 '
                  'Firefox/60.0Accept: text/html,application/xhtml+xml,'
                  'application/xml;q=0.9,*/*;q=0.8z'

}

req = Request(url='https://www.baidu.com',
              headers=headers)

resp = urlopen(req)
print(resp.status)
if resp.status == 200:
    print(resp.getheaders())
    print(resp.read().decode())

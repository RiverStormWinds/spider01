
# 浏览器对象， request.build_opener: 浏览器opener对象，  request.ProxyHandler: 代理服务器对象
# proxies: 代理服务器ip地址
# xpath：安装进chrome 进more tools--> extensions--> 然后把xpath拖入chrome--> ok
# 创建opener浏览器对象
import re
from urllib import request


def requestHTML(url):
    opener = request.build_opener(request.ProxyHandler(proxies={'https': '123.57.207.2:3128'}))
    req = request.Request(url)
    # resp = request.urlopen(req)
    resp = opener.open(req)
    if resp.status == 200:
        html = resp.read().decode('utf-8')
        return html


def parse_html(html):
    imgs = re.findall(r'<p><a target="_blank" href="(.*?)" alt="(.*?)"', html)
    for img, title in imgs:
        print(img)
        shtm1 = requestHTML(img)
        big_imgs = re.findall(r'<span class="img_open"><a href="(.*?)" title="(.*?)"', shtm1)
        for big_img in big_imgs:
            # print(big_img)
            download(big_img[0], big_img[1])


def download(img, title):
    request.urlretrieve(img, filename='../zhanzhangimg_big_img/{}.jpg'.format(title))
    # print(title, '图片下载完成')


def main():
    url = 'http://sc.chinaz.com/tupian/'
    html = requestHTML(url)
    parse_html(html)


if __name__ == '__main__':
    main()
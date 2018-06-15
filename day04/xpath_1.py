from urllib import request
from lxml import etree  # 虽然看着是有问题，但是能用


def request_html(url):

    headers = {
        'User-Agent': 'Mozilla / 5.0(X11;Ubuntu;Linuxx86_64;rv: 60.0) Gecko / 20100101Firefox / 60.0',
    }

    req = request.Request(url, headers=headers)

    resp = request.urlopen(req)

    if resp.status == 200:
        html = resp.read().decode()
        return html


def get_img(url):

    et = etree.HTML(request_html(url))

    titles = et.xpath("//div[@class='up']/div[@class='num_2']/a/@title")  # 图片链接的标题
    hrefs = et.xpath("//div[@class='up']/div[@class='num_2']/a/@href")  # 图片链接的超链接
    try:
        i = 0
        for href in hrefs:
            et_img = etree.HTML(request_html(href))
            img_datas = et_img.xpath("//div/img/@src")
            j = 0
            for img_data in img_datas:
                try:
                    request.urlretrieve(img_data, '../zhanzhangdongtu/{}.gif'.format(titles[i]+str(j)))
                    print('图片保存成功{}'.format(img_data), titles[i] + str(j) + '.gif')
                except Exception as e:
                    print(e)
                j = j + 1
            i = i + 1
    except Exception as e:
        print(e)

sum = 0
if __name__ == '__main__':
    # http://sc.chinaz.com/biaoqing/index_2.html
    # url = 'http://sc.chinaz.com/biaoqing/'
    i = 2
    url = 'http://sc.chinaz.com/biaoqing/'
    try:
        while True:
            # url = 'http://sc.chinaz.com/biaoqing/index_2.html'
            get_img(url)
            url = 'http://sc.chinaz.com/biaoqing/index_{}.html'.format(i)
            i = i + 1
            sum = sum + 1
    except Exception as e:
        print(e, '共{}个表情包'.format(sum))


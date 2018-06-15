from urllib import request
from lxml import etree  # 虽然看着是有问题，但是能用


def request_html(url):
    # request.urlretrieve(url, '1.html')

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

    # imgs = et.xpath('//img/@src2')  # 定位到小图

    # for img in imgs:
    #     print(img)

    # axpath = "//div[@class='up']/div[@class='num_2']/a"
    # titles = et.xpath('{}@title | {}@href'.format(axpath, axpath))

    titles = et.xpath("//div[@class='up']/div[@class='num_2']/a/@title")  # 图片链接的标题
    hrefs = et.xpath("//div[@class='up']/div[@class='num_2']/a/@href")  # 图片链接的超链接

# ////div/img[7]/@src
# <img src="http://pics.sc.chinaz.com/Files/pic/faces/5081/0.gif" class=" xh-highlight">

    i = 0
    for href in hrefs:
            et_img = etree.HTML(request_html(href))
            img_datas = et_img.xpath("//div/img/@src")
            j = 0
            for img_data in img_datas:
                request.urlretrieve(img_data, 'zhanzhangdongtu/{}.gif'.format(titles[i]+str(j)))
                print('图片保存成功', titles[i]+str(j)+'.gif')
                j = j + 1
            # i = i + 1


if __name__ == '__main__':

    url = 'http://sc.chinaz.com/biaoqing/'

    get_img(url)

    # request_html(url)

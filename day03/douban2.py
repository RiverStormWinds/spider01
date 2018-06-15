# https://movie.douban.com/j/chart/top_list
import json
import threading
import urllib
from threading import Thread
from urllib import parse, request
from multiprocessing import Process


class Douban_Top01:
    def __init__(self, lock, limit=20, start=0, type=5):

        self.url = 'https://movie.douban.com/j/chart/top_list'

        self.param = {
            'action': '',
            'interval_id': '100:90',
            'limit': limit,
            'start': start,
            'type': type,
        }

        self.params = urllib.parse.urlencode(self.param)

    # 声明请求头部
        self.header = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 '
                          'Firefox/60.0Accept: text/html,application/xhtml+xml,'
                          'application/xml;q=0.9,*/*;q=0.8z',
        }

    # 创建Request请求对象，生成post请求对象，data = b''
    def spider_req(self):
        req = request.Request(self.url, self.params.encode(), self.header)
        resp = request.urlopen(req)
        return resp

    # 写入
    def write_req(self):
        resp = self.spider_req()

        if resp.status == 200:
            print('请求成功')

            with open('../spider/douban-top-{}.json'.format(start / limit + 1), 'wb') as f:
                # 不加 b 会生成二进制字节码数据，加上b直接生成字符串
                f.write(resp.read())

    # 下载图片
    # 获取图片地址
    def write_img(self):
        bytes = self.spider_req().read()
        json_str = bytes.decode()  # 将bytes转成str
        # loads加载，将json字符串转换成json对象
        json_array = json.loads(json_str)  # 从json字符串中加载json数据，返回dict或list
        for movie in json_array:
            print('url', movie.get('cover_url'))
            print('名称', movie.get('title'), '当前线程', threading.current_thread().name)

            t1 = Thread(target=self.download_img, args=(movie.get('cover_url'), movie.get('title')))
            t1.start()
            t1.join()

    def download_img(self, url, title):
        with lock:
            request.urlretrieve(url, filename='../douban_images/{}.jpg'.format(title))
            print('线程名： ', threading.current_thread().name, 'url: ', url)


if __name__ == '__main__':

    lock = threading.Lock()

    for i in range(20):
        limit = 20
        start = i * limit
        doubans = []

        for j in range(29):
            print(j)
            doubans.append(Douban_Top01(lock, start=start, type=j))

        # p1 = Process(target=douban.write_img)
        # p2 = Process(target=douban2.write_img)

        # p1.start()
        # p2.start()

        # p1.join()
        # p2.join()

        procs = [Process(target=doubans[k].write_img) for k in range(29)]
        # 五个进程直接一起搞f函数，就传进去一个user = manager.User('disen', 100)对象和进程锁lock
        for proc in procs:
            proc.start()

        for proc in procs:
            proc.join()


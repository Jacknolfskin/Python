# -*- coding: utf-8 -*-
import sys
import time
import threading
import requests
import random
import uuid
import logging
"""

Post请求压测

"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='测试脚本日志.log',
                    filemode='w')

add = "192.168.5.10"
port = 80
thread_count = 3  # 单次并发数量
request_interval = 2 # 请求间隔(秒)
test_count = 5  # 指定测试次数
t_objs = []  # 存线程实例

now_count = 1

lock_obj = threading.Lock()

urls = [
    "http://api.zkteco.com/admin/a.html",
    "http://api.zkteco.com/admin/a.html",
    "http://api.zkteco.com/admin/a.html",
]


def send_http():
    global now_count
    global urls
    url = urls[random.randint(0, len(urls) - 1)]
    httpClient = None

    try:
        httpClient = requests.request('get', url)

        print('返回码:', str(httpClient.status_code))
        print('返回数据:', httpClient.text)
        # print('返回原始数据:',httpClient.raw.read)

        logging.info('返回码:' + str(httpClient.status_code))
        logging.info('返回数据:' + httpClient.text)

        sys.stdout.flush()
        now_count += 1

    except Exception as e:
        print(e)
        logging.info(e)

    finally:
        if httpClient:
            httpClient.close()


def test_func(run_count):
    global now_count
    global request_interval
    global lock_obj
    cnt = 0

    while cnt < run_count:
        lock_obj.acquire()
        print('')
        print('***************************请求次数:' + str(cnt) + '*******************************')
        print('Thread:(%d) Time:%s\n' % (threading.get_ident(), time.ctime()))

        # logging.info('')
        # logging.info('***************************请求次数:' + str(now_count) + '*******************************')
        # logging.info('Thread:(%d) Time:%s\n' % (threading.get_ident(), time.ctime()))

        cnt += 1
        start_time = time.time()
        send_http()
        end_time = time.time() - start_time
        print("*****************请求时间:" + str(end_time) + "*********************")
        sys.stdout.flush()
        lock_obj.release()
        time.sleep(request_interval)


def test(ct):
    global thread_count
    for i in range(thread_count):
        t = threading.Thread(target=test_func, args=(ct,))
        t.start()
        t_objs.append(t)

    for t in t_objs:
        t.join()


if __name__ == '__main__':
    test(test_count)

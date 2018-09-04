import urllib
import datetime
import threading
from time import ctime, sleep

"""

Get请求压测

"""
def t1(func):
    for i in range(50):
        starttime = datetime.datetime.now()
        url = "http://localhost:8080/api/test?pid=10000&mobile=%s%03d%02d&type=abc" % ('135000', func, i)
        f = urllib.urlopen(url)
        s = f.read()
        endtime = datetime.datetime.now()
        print("round:%s, tread number:%s, returnValue:%s,time:%f" % (
            i, func, s, (endtime - starttime).microseconds / 1000))
        sleep(1)


if __name__ == '__main__':
    threads = []
    for i in range(50):
        name = "t%s" % (i)
        name = threading.Thread(target=t1, args=(i,))
        threads.append(name)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

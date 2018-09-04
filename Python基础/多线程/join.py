import sys
import threading, time

t_objs = []  # 存线程实例
thread_count = 3  # 单次并发数量
test_count = 2  # 指定测试次数


# lock_obj = threading.Lock()


def Myjoin(run_count):
    # global lock_obj
    cnt = 0
    while cnt < run_count:
        # lock_obj.acquire()
        print('***************************请求次数:' + str(cnt) + '*******************************')
        cnt += 1
        print('hello world!')
        sys.stdout.flush()
        # lock_obj.release()
        time.sleep(2)


def test(ct):
    global thread_count
    for i in range(thread_count):
        t = threading.Thread(target=Myjoin, args=(ct,))
        t.start()
        t_objs.append(t)
        # t.join()

    for t in t_objs:
        t.join()


if __name__ == '__main__':
    test(test_count)
    print('hello main')

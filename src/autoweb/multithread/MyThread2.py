import threading
from datetime import datetime
import time


def thread_func():  # 线程函数#
    time.sleep(2)
    i = 0
    while i < 11:
        print(datetime.now())
        i += 1
    print('func exit')


def many_thread():
    threads = []
    for _ in range(3):  # 循环创建500个线程
        t = threading.Thread(target=thread_func)
        threads.append(t)
#        t.setDaemon(True)
    for t in threads:  # 循环启动500个线程
        t.start()
#    for t in threads:
#        t.join()


if __name__ == '__main__':
    many_thread()
    print("thread end")

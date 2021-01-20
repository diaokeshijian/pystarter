import threading
import time


def run(tx):
    print("task", tx)
    time.sleep(1)
    print(tx + '2s')
    time.sleep(1)
    print(tx + '1s')
    time.sleep(1)
    print(tx + '0s')
    time.sleep(1)


t1 = threading.Thread(target=run, args=('t1',))
t2 = threading.Thread(target=run, args=('t2',))

t1.start()
t2.start()

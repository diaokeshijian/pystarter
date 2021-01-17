import time

counter = 0
while True:
    with open('D:\\timer.txt', 'a') as f:
        line = 'time passed ' + str(counter) + ' seconds...'
        f.write(line)
        f.write('\n')
        time.sleep(10)
        counter = counter + 10
        print(counter)

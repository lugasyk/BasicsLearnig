from threading import current_thread
from multiprocessing.pool import ThreadPool


def run(max_value=100):
    print('Fibonacci go!')
    print('Hello from {} Thread!'.format(current_thread()))
    nextvalue = 0
    firstvalue = 0
    secondvalue = 1
    for i in range(max_value):
        if i <= 1:
            nextvalue == i
        else:
            nextvalue = firstvalue + secondvalue
            firstvalue = secondvalue
            secondvalue = nextvalue
        print(nextvalue)
    print('Fibonacci ended')


pool = ThreadPool(5)

try:
    pool.map(run, range(10))
finally:
    pool.close()

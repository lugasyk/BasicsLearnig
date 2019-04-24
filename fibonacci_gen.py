from threading import Thread, current_thread
from multiprocessing.pool import ThreadPool


class FibonacciThread(Thread):
    #def __init__(self):
        #Thread.__init__(self)



print("Main Thread Started")
MyFibonacciThread = FibonacciThread()
MyFibonacciThread.start()
FirstThread = FibonacciThread()
FirstThread.start()
print("Main Thread Started to wait for the Fibonacci Thread to complete")
MyFibonacciThread.join()
print("Main Thread Resumed")
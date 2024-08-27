#Multithreading
#I/O-bound tasks
###Concurrent executions

import threading
import time

def print_number():
    for i in range(1, 6):
        time.sleep(2)
        print(f"Number:{i}")


def print_letter():
    for letter in "ABCDEFGHIJ":
        time.sleep(2)
        print(f"Letter:{letter}")

#Create 2 threads 
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_letter)


t=time.time()
#Start the thread 
t1.start()
t2.start()

#Wait until the threads are completely executed
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)
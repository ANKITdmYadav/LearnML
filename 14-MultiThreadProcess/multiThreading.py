import threading
import time
def print_num():
    for i in range(10):
        time.sleep(1)
        print(i)

def print_char():
    for i in "ABCDEFGHIJ":
        time.sleep(1)
        print(i)

t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_char)
startt=time.time()
t1.start()
t2.start()
t1.join()
t2.join()
endd=time.time()
print(endd-startt)

# print_num()
# print_char()

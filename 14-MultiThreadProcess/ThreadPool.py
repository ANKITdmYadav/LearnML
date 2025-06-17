import threading,time
from concurrent.futures import ThreadPoolExecutor
def print_num(number):
    time.sleep(1)
    return number
number=[1,2,3,4,5,6,7,8,9,0]
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_num,number)
for i in results:
    print(i)


# import multiprocessing
# from concurrent.futures import ProcessPoolExecutor
# with ProcessPoolExecutor(max_workers=3) as executor:

import multiprocessing.pool
import multiprocessing,math,time,sys

sys.set_int_max_str_digits(100000)

def compute_fact(num):
    result=math.factorial(num)
    print(f"factorial of {num} is {result}")
    return result

if __name__=="__main__":
    number=[4000,5000,6000]
    startt=time.time()
    with multiprocessing.Pool() as pool:
        result=pool.map(compute_fact,number)
    endd=time.time()
    # print(f"result is {result}")
    print(f"time taken is {endd-startt}")


from logger import logging

def add(a,b):
    result=a+b
    logging.debug(f"The addition operation is taking place {result}")
    return a+b


logging.debug("The addition function is called")
add(10,15)
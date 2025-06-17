import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[ logging.FileHandler("app1.log"),
                logging.StreamHandler()
    ]
)

logger=logging.getLogger("ArithematicApp")
def add(a,b):
    result=a+b
    logger.debug(f" sum is {result}")
    return result

def divide(a,b):
    try:
        result=a/b
        logger.debug(f"division {result}")
        return result
    except ZeroDivisionError:
        logger.error("Zero division error")
        return None

divide(5,0)
        
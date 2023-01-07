from time_laps import time_laps
from time_laps import logger


@time_laps
def calc(num):
    sumNum = 0
    for i in range(num):
        sumNum += i
        logger.debug(sumNum)
    print(sumNum)


calc(100000000)

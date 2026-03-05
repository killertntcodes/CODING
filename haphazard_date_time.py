import random
import time
def random_date(start_date, end_date):
    print("printing random date between", start_date, "and", end_date)
    randomGen = random.random()
    dateformat = "%m/%d/%Y"
    startTIME= time.mktime(time.strptime(start_date, dateformat))
    endTIME= time.mktime(time.strptime(end_date, dateformat))
    randomTIME = startTIME + randomGen * (endTIME - startTIME)
    randomDATE = time.strftime(dateformat, time.localtime(randomTIME))
    return randomDATE
print("Random date generated:", random_date("1/1/2016", "12/12/2018"))
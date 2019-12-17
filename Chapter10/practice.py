# 1 
today = '2019-12-17'

f = open('./today.txt', 'w')
f.write(today)
f.close()

# 2
f = open('./today.txt', 'r')
today_string = f.read()


# 3
import datetime
date = datetime.datetime.strptime(today_string, "%Y-%m-%d").date()

# 4
# import os
# print(os.listdir())

# import multiprocessing
# import time
# import random
# def timestamp():
#     print(os.getpid())
#     time.sleep(random.randint(1, 5))
#     print(datetime.datetime.now())

# if __name__ == '__main__':    
#     for i in range(3):
#         p = multiprocessing.Process(target=timestamp, args=())
#         p.start()


# 7 
birth = datetime.datetime.strptime('1995-06-23', "%Y-%m-%d")

# 8
day = ['월', '화', '수', '목', '금', '토', '일']
print(day[birth.weekday()])

delta = datetime.timedelta(days=10000)
print(birth + delta)
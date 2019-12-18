# 스레드는 한 프로세스 내에서 실행, 모든 프로세스의 자원에 접근 가능, 다중 인격과 비슷?
# mp가 프로세스 기반의 대응으로 나중에 설계된 모듈.

# 스레드가 위험한 이유는 모든 코드에 문제를 일으킬 수 있다. 따라서 스레드세이프한 코드를 짜야 한다. 전역 변수와 같은 것들은
# 큰 문제를 야기할 수 있다. 즉, 스레드는 전역 데이터가 관여하지 않을 때 안전하고 유용하다. 별개의 데이터를 가질 경우 안전!
# mp는 집으로 치면 각기 다른 집을 가지고 있는 것, td는 한 집에 각기 다른 사람이 있는 것으로 비유 가능.
# 그래도, 전역 데이터를 스레드간 공유하면서 작업을 나누어 작업할 수도 있겠다. 스레드마다 처리 한 후 전역 데이터값 변경으로 
# 모든 스레드가 알아챌 수 있겠음.

# ※ 파이썬의 스레드는 cpu 바운드 작업을 빠르게 처리하지 못함, GIL(Global Interpreter Lock) 표준 때문이다. GIL은 파이썬 인터프리터의 
# 스레딩 문제를 피하기 위해 존재. 따라서, 싱글 스레드, 멀티 프로세스보다 느릴 수 있음.

# 책의 권고 사항은 
# I/O 바운드 문제 ==> 쓰레드 사용
# CPU 바운드 문제 ==> 프로세스, 네트워킹, 이벤트 사용


# dish.py 스레드 기반
import threading, queue
import time

def washer(dishes, q):
    for dish in dishes:
        print('wash!', dish)
        time.sleep(5)
        q.put(dish)

def dryer(q):
    while q:
        dish = q.get()
        print('dryer', dish)
        time.sleep(7)
        q.task_done()


dish_q = queue.Queue()
for n in range(2):
    dryer_thraed = threading.Thread(target=dryer, args=(dish_q, ))
    dryer_thraed.start()

dishes = ['떡볶이', '김밥', '돈가스', '치킨']
washer(dishes, dish_q)
dish_q.join()


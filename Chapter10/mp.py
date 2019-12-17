import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process %s says %s" % (os.getpid(), what))

if __name__ == '__main__':
    whoami("I am the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=("Multiprocess! I am function %s" % n, ))
        p.start()

    
    for n in range(4):
        import threading
        t = threading.Thread(target=do_this, args=("Thread! I am function %s" % n, ))
        t.start()


    # Thread vs multiprocess
    # Thread의 경우 동일한 pid(프로세스)로 실행이 되고, multiprocess의 경우 각기 다른 pid()를 가진다.
    # 즉, 멀티프로세스의 경우 파이썬 함수를 각기 다른 프로세스를 이용해 실행하고, 스레드는 동일한 프로세스를 통해 실행한다.

    # Thread는 한 프로세스 내에서 실행되는 것. 프로세스의 모든 자원에 접근 가능


    # multiprocess는 하나의 작업을 여러 프로세스에 할당 가능 ex) 크롤링 따로, 이미지 크기 조정 따로 가능
    # muiltiprocessing()은 프로세스 간의 상호 통신과 모든 프로세스가 끝날 때까지 기다리는 큐 작업 포함


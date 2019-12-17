# 하나의 프로그램 실행할 때 OS는 한 프로세스 생성, 프로세스는 OS와 Kernel(파일과 네트워크 연결)에서 시스템 리소스(CPU, 메모리, 디스크 공간) 및 자료구조 사용 
#
# 한 프로세스는 다른 프로세스에 독립됨 (독립성)
# 프로세스 간에 서로 뭐 하는지 알 수나 방해 할 수 없다.

# OS는 실행 중인 모든 프로세스 추적함
# 한 프로세스를 확인하고 다음 프로세스를 확인하고 하는 방식이다, 

# 운영체제는 두 가지 목표가 있다.
# 1. 프로세스를 공정하게 실행하여 되도록 많은 프로세스가 실행되게 함. 
# 2. 사용자의 명령을 반응적으로 처리하는 것.

# 작업 관리자를 확인하면 현재 실행중인 프로세스 상태 확인 가능.

# 내 자신의 프로그램에서 프로세스 데이터에 접근할 수 있다. (os 모듈 활용)

'''
    실습
'''
# 실행 중인 파이썬 인터프리터에 대한 프로세스 ID와 현재 작업 디렉터리 확인해 보자.
import os
print(os.getpid()) # pid 확인
print(os.getcwd()) # 작업 디렉터리 확인

# print(os.getuid(), os.getgid())  
# 사용자 id, 그룹 id 확인 가능 (유닉스 버전)


# 프로세스 생성 : subprocess()
# subprocess 모듈을 통해 존재하는 다른 프로그램을 시작하거나 멈출 수 있다.
# 프로그램 실행 결과를 확인하고 싶으면 getoutput() 함수

import subprocess
'''
# getoutput()의 인자는 쉘 명령의 문자열이기 때문에 인자, 파이프, I/O 리다이렉션 포함 가능
# getstatusoutput()을 사용하면 해당 프로그램의 상태 코드와 결과를 (상태코드, 결과) 튜플로 반환
res = subprocess.getoutput('date') 
print(res) # 프로세스가 끝날 때까지 아무런 결과를 얻지 못함 (병행성 X)
'''

# 프로세스 생성(2) : multiprocessing

# multiprocessing 함수를 이용하면 파이썬 함수를 별도의 프로세스로 실행하거나 한 프로그램에서 독립적인 여러 프로세스 실행 가능

# mp.py 참조


# terminate() 프로세스 죽이기
# 무한 루프에 빠진 프로세스,, 등을 종료하기 위해서는 터미네이터 형님이 필요하겠다.

# 다음 예제는 100만 개의 프로세스 생성, 각 스텝마다 1초 동안 아무런 일도 하지 않으며 울화통 터진다. 
# 메인 프로그램의 인내 부족으로 5초 동안만 실행

import multiprocessing
import time

def whoami(name):
    print(os.getpid(), "my name is ", name)

def loopy(name):
    whoami(name)

    start = 1
    stop = 100000
    for num in range(start, stop):
        print("\t NUMBER %s of %s. Honk!" % (num, stop))

if __name__ == '__main__':
    whoami("Main")

    p = multiprocessing.Process(target=loopy, args=("loopy", ))
    p.start()
    time.sleep(5)
    p.terminate() # 죽여버린다.


# 또한, thread는 terminate() 또한 없다.
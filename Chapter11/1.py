# 성능, 견고함, 간소화, 커뮤니케이션

# 컴퓨터가 일을 수행하면서 기다리는 이유는 보통 둘 중 하나.
# I/O 바운드 - CPU는 매우 빠르다, 메모리보다 몇 백 배, 네트워크·디스크보다 몇 천 배 빠르다.
# CPU 바운드 - 과학이나 그래픽 작업과 같은 엄청난 계산이 필요할 때

# 동기 vs 비동기
# 동기는 한 줄의 장례
# 비동기는 각각 독립적

# 웹에서 이미지 크기를 조정해야 하는 코드가 생긴다면, 이는 이를 위한 전용 프로세스를 호출할 수 있다. (수평적)

# 여러 작업을 관리할 수 있는 “큐”를 이용해 서로 같이 처리할 수 있게 하자.

# 일반적으로 큐는 메세지를 전달. 메세지는 모든 종류의 정보가 될 수 있다.

# 프로세스
# 큐를 여러 가지 방법으로 구현할 수 있는데, 싱글 머신에서의 표준 라이브러리 multiprocessing 모듈의 Queue도 존재.
# 한 대의 식기세척기와 여러 대의 건조기 프로세스 시뮬해 보자.
 
# dish.py 참조
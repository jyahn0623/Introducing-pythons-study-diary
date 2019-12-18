# 네트워킹 및 분산 컴퓨팅

# 패턴
# 몇 가지 기본 패턴으로 네트워킹 어플리케이션 생성 가능

# 1. 요청-응답 패턴 (클라이언트-서버 패턴)
# 2. 푸시 또는 팬아웃 패턴
# 3. 발행·구독 패턴  
#  - 발행자가 데이터 전송
#  - 모든 구독자는 데이터의 복사본 받음
#  - 구독자는 데이터(토픽)에 관심 있음을 표시할 수 있다.
#  - 발행자는 단지 토픽만을 전송.
#  - 토픽에 대한 구독자가 없을 경우 데이터는 무시

#  TCP/IP
#  -
#  IP 계층 (UDP, TCP 프로토콜 존재)
#  - UDP : 짧은 데이터 교환에 사용, 데이터그램은 한 단위로 전송되는 작은 메세지
#  - TCP : 수명이 긴 커넥션에 사용, TCP는 바이트 스트림이 중복없이 순서대로 도착하는 것을 보장
 
#  UDP는 ACK(응답 메세지)가 없어 잘 도착했는지 확인할 수 없음., 비연결형, 비신뢰성, 빠르고, 가볍다.
#  TCP는 송신자와 수신자 사이의 커넥션 보장을 위해 핸드셰이크 설정


#  소켓
#  · 네트워크 프로그래밍의 가장 낮은 수준은 C 언어와 유닉스 OS에서 빌려온 소켓 사용 (소켓 레벨 프로그래밍은 지루..)
 
from datetime import datetime
import socket

server_address = ('127.0.0.1', 8009)
max_size = 4096

print('starting server at', datetime.now())
print('waiting call from client')

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

print('At', datetime.now(), 'data: ', data, 'said by', client)
server.sendto(b'Are you tlaking to me?', client)
server.close()
# 이진 데이터 변환하기 : struct 

# C, C++과 유사한 구조체 방식
# png 파일의 가로·세로의 길이를 구해보장.


# 빅 엔디안은 왼쪽에서부터 최상위 바이트 저장

# struct.unpack() -> 바이트 시퀀스를 해석하고 파이썬 데이터 형식으로 바꾸어 줌
# struct.pack() -> 파이썬 형식을 바이트로 변환
import struct

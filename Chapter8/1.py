# readline() : 한 글자씩 읽음
# readlines() : 각 라인을 iterator로 반환
# read() : 전체를 한 번에 읽음, 큰 경우 메모리 많이 먹음

_f = open('./info.txt', 'w', encoding='utf-8')
_f.write('안녕하세요, 만나서 반갑습니다. \n')
_f.write('제 이름은 안주영이라고 합니다.')
_f.close()

_rf = open('./info.txt', 'r', encoding='utf-8')
_rf.close()

# with 사용 시 명시적으로 닫지 안더라도 지가 알아서 닫기게 함. 

# seek() : 파일 위치 찾기

# 2진 파일 쓰기
bdata = bytes(range(0, 256))

_f  = open('bfile', 'wb')
_f.write(bdata)
_f.close()

# 2진 파일 읽기
with open('bfile', 'rb') as f:
    # 256 바이트의 이진 파일임 "bfile"은
    print(f.tell()) # tell() 파일의 시작으로부터 현재 오프셋을 바이트 단위로 반환
    print(f.seek(255)) # 파일의 마지막에서 1바이트 (255 = 8비트 = 1바이트 ) 전 위치로 이동

    print(f.read()) # read 결과 마지막 바이트만 읽어지는 것을 확인할 수 있음.

# seek(offset, origin) origin 0 : 시작 위치에서 offset 바이트 이동, origin 1 : 현재 위치에서 offset 바이트 이동 origin 2 : 마지막 위치에서 offset 바이트 전 위치로 이동
with open('bfile', 'rb') as f:
    f.seek(-2, 2) # 파일 마지막에서 2바이트 전 위치로 이동
    print(f.tell())

    print(f.read()[0])

